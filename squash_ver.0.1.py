import sys
import math
from random import randint
import pygame

WIDTH = 600
HEIGHT = 600

INIT_SPEED = 12
BALL_SIZE = 20
BALL_COLOR = (255, 255, 255)

RACKET1_SIZE = (110, 550, 80, 10)
RACKET1_COLOR = (0, 0, 255)

RACKET2_SIZE = (410, 550, 80, 10)
RACKET2_COLOR = (255, 0, 0)

BORDER_TOP_SIZE = (0, 0, 600, 5)
BORDER_BOTTOM_SIZE = (0, 595, 600, 5)
BORDER_LEFT_SIZE = (0, 0, 5, 600)
BORDER_RIGHT_SIZE = (595, 0, 5, 600)
BORDER_CENTER_SIZE = (300, 450, 1, 150)
BORDER_COLOR = (255, 255, 255)

ANGLE = 30

def main():
    pygame.init()
    pygame.key.set_repeat(10, 10)
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('超速スカッシュ')

    font = pygame.font.Font(None, 80)
    message_over = font.render('You are out!', True, (255, 0, 0))
    message_pos = message_over.get_rect()

    message_pos.centerx = surface.get_rect().centerx
    message_pos.centery = 200
    ball_num = 5
    racket1 = pygame.Rect(RACKET1_SIZE)

    ball = pygame.Rect(surface.get_rect().centerx - 10, 0, BALL_SIZE, BALL_SIZE)

    racket2 = pygame.Rect(RACKET2_SIZE)

    border_top = pygame.Rect(BORDER_TOP_SIZE)
    border_bottom = pygame.Rect(BORDER_BOTTOM_SIZE)
    border_left = pygame.Rect(BORDER_LEFT_SIZE)
    border_right = pygame.Rect(BORDER_RIGHT_SIZE)
    border_center = pygame.Rect(BORDER_CENTER_SIZE)

    direction = randint(ANGLE, 180 - ANGLE)
    speed = INIT_SPEED
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and racket1.top > 450:
                    racket1.centery -= 10
                if event.key == pygame.K_s and racket1.bottom < HEIGHT:
                    racket1.centery += 10
                if event.key == pygame.K_a and racket1.left > 0: #and ball.centerx < 300
                    racket1.centerx -= 10
                if event.key == pygame.K_d and racket1.right < 300: #and ball.centerx < 300
                    racket1.centerx += 10
                if event.key == pygame.K_UP and racket2.top > 450:
                    racket2.centery -= 10
                if event.key == pygame.K_DOWN and racket2.bottom < HEIGHT:
                    racket2.centery += 10
                if event.key == pygame.K_LEFT and racket2.left > 300: #and ball.centerx > 300
                    racket2.centerx -= 10
                if event.key == pygame.K_RIGHT and racket2.right < WIDTH: #and ball.centerx > 300
                    racket2.centerx += 10
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if ball.centery < HEIGHT:
            ball.centerx += int(math.cos(math.radians(direction)) * speed)
            ball.centery += int(math.sin(math.radians(direction)) * speed)
        else:
            if ball_num > 1:
                ball_num -= 1
                ball.left = 50
                ball.top = 50
                direction = randint(ANGLE, 180 - ANGLE)
            else:
                game_over = True

        if racket1.colliderect(ball):
            direction = -(90 + (racket1.centerx - ball.centerx) / racket1.width * 100)

        if racket2.colliderect(ball):
            direction = -(90 + (racket2.centerx - ball.centerx) / racket2.width * 100)

        if ball.centerx < 0 or ball.centerx > WIDTH:
            direction = 180 - direction

        if ball.centery < 0:
            direction = -direction

        surface.fill((0, 255, 0))

        if game_over:
            surface.blit(message_over, (message_pos))

        pygame.draw.rect(surface, BORDER_COLOR, border_top)
        pygame.draw.rect(surface, BORDER_COLOR, border_bottom)
        pygame.draw.rect(surface, BORDER_COLOR, border_left)
        pygame.draw.rect(surface, BORDER_COLOR, border_right)
        pygame.draw.rect(surface, BORDER_COLOR, border_center)

        pygame.draw.rect(surface, RACKET1_COLOR, racket1)
        pygame.draw.rect(surface, RACKET2_COLOR, racket2)

        pygame.draw.ellipse(surface, BALL_COLOR, ball)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
