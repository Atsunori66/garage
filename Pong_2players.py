import sys
import math
from random import randint, choice
import pygame

WIDTH = 700
HEIGHT = 400

INIT_SPEED = 13
BALL_SIZE = 20
BALL_COLOR = (255, 255, 255)

SWING = 25
RACKET1_SIZE = (10, 180, 10, 90)
RACKET1_COLOR = (255, 255, 255)

RACKET2_SIZE = (WIDTH - 20, 180, 10, 90)
RACKET2_COLOR = (255, 255, 255)

BORDER_TOP_SIZE = (0, 0, WIDTH, 5)
BORDER_BOTTOM_SIZE = (0, HEIGHT - 5, WIDTH, 5)
BORDER_LEFT_SIZE = (0, 0, 5, 600)
BORDER_RIGHT_SIZE = (WIDTH - 5, 0, 5, HEIGHT)

BORDER_COLOR = (255, 255, 255)

def main():
    pygame.init()
    pygame.key.set_repeat(1, 1)
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Pong!')

    end_font = pygame.font.Font(None, 60)
    message_over1 = end_font.render('Player 2 wins!', True, (255, 0, 255))
    message_pos1 = message_over1.get_rect()
    message_pos1.centerx = int(WIDTH / 2)
    message_pos1.centery = int(HEIGHT / 2)

    message_over2 = end_font.render('Player 1 wins!', True, (0, 255, 255))
    message_pos2 = message_over2.get_rect()
    message_pos2.centerx = int(WIDTH / 2)
    message_pos2.centery = int(HEIGHT / 2)

    ball = pygame.Rect(surface.get_rect().centerx, surface.get_rect().centery, BALL_SIZE, BALL_SIZE)
    racket1 = pygame.Rect(RACKET1_SIZE)
    racket2 = pygame.Rect(RACKET2_SIZE)

    border_top = pygame.Rect(BORDER_TOP_SIZE)
    border_bottom = pygame.Rect(BORDER_BOTTOM_SIZE)
    border_left = pygame.Rect(BORDER_LEFT_SIZE)
    border_right = pygame.Rect(BORDER_RIGHT_SIZE)

    direction = choice([randint(0, 80), randint(100, 260), randint(280, 360)])

    speed = INIT_SPEED

    life1 = 5
    life2 = 5

    racket2_count = 0

    game_over_1 = False
    game_over_2 = False

    while True:
        life_font = pygame.font.Font(None, 36)

        life1_show = life_font.render('Player 1: ' + str(life1), True, (255, 255, 255))
        life1_pos = life1_show.get_rect()
        life1_pos.centerx = 240
        life1_pos.centery = 40

        life2_show = life_font.render('Player 2: ' + str(life2), True, (255, 255, 255))
        life2_pos = life2_show.get_rect()
        life2_pos.centerx = 460
        life2_pos.centery = 40

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and racket1.top > 15:
                    racket1.centery -= SWING
                if event.key == pygame.K_s and racket1.bottom < HEIGHT - 15:
                    racket1.centery += SWING
                if event.key == pygame.K_a and racket1.left > 10:
                    racket1.centerx -= SWING
                if event.key == pygame.K_d and racket1.right < 100:
                    racket1.centerx += SWING
                if event.key == pygame.K_UP and racket2.top > 15:
                    racket2.centery -= SWING
                if event.key == pygame.K_DOWN and racket2.bottom < HEIGHT - 15:
                    racket2.centery += SWING
                if event.key == pygame.K_LEFT and racket2.left > 600:
                    racket2.centerx -= SWING
                if event.key == pygame.K_RIGHT and racket2.right < WIDTH - 10:
                    racket2.centerx += SWING
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if racket1.colliderect(ball):
            direction = -(racket1.centery - ball.centery)
            speed += 0.2
        if racket2.colliderect(ball):
            direction = 180 + (racket2.centery - ball.centery)
            speed += 0.2

        if ball.centery < 0 or ball.centery > HEIGHT:
            direction = -direction
            speed += 0.6
        if ball.centerx >= 0 and ball.centerx <= WIDTH:
            ball.centerx += int(math.cos(math.radians(direction)) * speed)
            ball.centery += int(math.sin(math.radians(direction)) * speed)
        else:
            if life1 >= 1 and life2 >= 1:
                if ball.centerx < 0:
                    life1 -= 1
                    ball.left = int(WIDTH / 2)
                    ball.top = int(HEIGHT / 2)
                    direction = choice([randint(0, 80), randint(100, 260), randint(280, 360)])
                    speed = INIT_SPEED
                if ball.centerx > WIDTH:
                    life2 -= 1
                    ball.left = int(WIDTH / 2)
                    ball.top = int(HEIGHT / 2)
                    direction = choice([randint(0, 80), randint(100, 260), randint(280, 360)])
                    speed = INIT_SPEED

            if life1 < 1:
                game_over_1 = True
            if life2 < 1:
                game_over_2 = True

        surface.fill((0, 0, 0))

        if game_over_1:
            surface.blit(message_over1, (message_pos1))
        if game_over_2:
            surface.blit(message_over2, (message_pos2))

        pygame.draw.rect(surface, BORDER_COLOR, border_top)
        pygame.draw.rect(surface, BORDER_COLOR, border_bottom)
        pygame.draw.rect(surface, BORDER_COLOR, border_left)
        pygame.draw.rect(surface, BORDER_COLOR, border_right)

        pygame.draw.rect(surface, RACKET1_COLOR, racket1)
        pygame.draw.rect(surface, RACKET2_COLOR, racket2)

        pygame.draw.ellipse(surface, BALL_COLOR, ball)

        surface.blit(life1_show, (life1_pos))
        surface.blit(life2_show, (life2_pos))

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
