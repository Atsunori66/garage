import sys
import math
import pygame
from random import randint, choice

WIDTH = 700
HEIGHT = 400

INIT_SPEED = 12
BALL_SIZE = 20
BALL_COLOR = (255, 255, 255)

RACKET_LENGTH = 90

SWING = 24
RACKET1_SIZE = (10, int((HEIGHT - RACKET_LENGTH) / 2), 10, RACKET_LENGTH)
RACKET1_COLOR = (255, 255, 255)

CPU_SWING = 8
RACKET2_SIZE = (WIDTH - 20, int((HEIGHT - RACKET_LENGTH) / 2), 10, RACKET_LENGTH)
RACKET2_COLOR = (255, 0, 0)

BORDER_TOP_SIZE = (0, 0, WIDTH, 5)
BORDER_BOTTOM_SIZE = (0, HEIGHT - 5, WIDTH, 5)
BORDER_CENTER_SIZE = (int(WIDTH / 2) - 2, 0, 4, HEIGHT)
BORDER_LEFT_SIZE = (0, 0, 5, 600)
BORDER_RIGHT_SIZE = (WIDTH - 5, 0, 5, HEIGHT)

BORDER_COLOR = (255, 255, 255)

def main():
    pygame.init()
    pygame.key.set_repeat(10, 10)
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Pong Pong Pong!!')

    end_font = pygame.font.Font(None, 50)
    message_win1 = end_font.render('You win!', True, (255, 255, 255))
    message_pos1 = message_win1.get_rect()
    message_pos1.centerx = int(WIDTH / 4)
    message_pos1.centery = int(HEIGHT / 2)

    message_win2 = end_font.render('You lose...', True, (255, 255, 255))
    message_pos2 = message_win2.get_rect()
    message_pos2.centerx = int(WIDTH * 3 / 4)
    message_pos2.centery = int(HEIGHT / 2)

    ball = pygame.Rect(surface.get_rect().centerx, surface.get_rect().centery, BALL_SIZE, BALL_SIZE)
    racket1 = pygame.Rect(RACKET1_SIZE)
    racket2 = pygame.Rect(RACKET2_SIZE)

    border_top = pygame.Rect(BORDER_TOP_SIZE)
    border_bottom = pygame.Rect(BORDER_BOTTOM_SIZE)
    border_center = pygame.Rect(BORDER_CENTER_SIZE)
    border_left = pygame.Rect(BORDER_LEFT_SIZE)
    border_right = pygame.Rect(BORDER_RIGHT_SIZE)

    direction = choice([randint(60, 80), randint(100, 120), randint(240, 260), randint(280, 300)])

    speed = INIT_SPEED

    score1 = 0
    score2 = 0

    victory_1 = False
    victory_2 = False

    while True:
        score_font = pygame.font.Font(None, 36)

        score1_show = score_font.render('You: ' + str(score1), True, (255, 255, 255))
        score1_pos = score1_show.get_rect()
        score1_pos.centerx = int(WIDTH / 4)
        score1_pos.centery = 40

        score2_show = score_font.render('COM: ' + str(score2), True, (255, 255, 255))
        score2_pos = score2_show.get_rect()
        score2_pos.centerx = int(WIDTH * 3 / 4)
        score2_pos.centery = 40

        if ball.centerx > WIDTH / 2:
            if racket2.centery > ball.centery:
                racket2.centery -= CPU_SWING
            elif racket2.centery < ball.centery:
                racket2.centery += CPU_SWING

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and racket1.top > 15:
                    racket1.centery -= SWING
                if event.key == pygame.K_DOWN and racket1.bottom < HEIGHT - 15:
                    racket1.centery += SWING
                if event.key == pygame.K_LEFT and racket1.left > 10:
                    racket1.centerx -= SWING
                if event.key == pygame.K_RIGHT and racket1.right < 100:
                    racket1.centerx += SWING
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if racket1.colliderect(ball):
            direction = -(racket1.centery - ball.centery) + randint(-20, 20)
            speed += 0.1
        if racket2.colliderect(ball):
            direction = 180 + (racket2.centery - ball.centery) + randint(-20, 20)
            speed += 0.1

        if ball.centery < 0 or ball.centery > HEIGHT:
            direction = -direction
            speed += 0.3

        if ball.centerx >= 0 and ball.centerx <= WIDTH:
            ball.centerx += int(math.cos(math.radians(direction)) * speed)
            ball.centery += int(math.sin(math.radians(direction)) * speed)
        else:
            if (score1 < 11 and score2 < 11) or (score1 >=11 and score1 < score2 + 2) or (score2 >= 11 and score2 < score1 + 2):
                if ball.centerx > WIDTH:
                    score1 += 1
                    ball.left = int(WIDTH / 2)
                    ball.top = int(HEIGHT / 2)
                    direction = choice([randint(60, 80), randint(100, 120), randint(240, 260), randint(280, 300)])
                    speed = INIT_SPEED
                if ball.centerx < 0:
                    score2 += 1
                    ball.left = int(WIDTH / 2)
                    ball.top = int(HEIGHT / 2)
                    direction = choice([randint(60, 80), randint(100, 120), randint(240, 260), randint(280, 300)])
                    speed = INIT_SPEED
            if score1 >= 11 and score1 >= score2 + 2:
                victory_1 = True
            if score2 >= 11 and score2 >= score1 + 2:
                victory_2 = True

        surface.fill((0, 100, 200))

        if victory_1:
            surface.blit(message_win1, (message_pos1))
        if victory_2:
            surface.blit(message_win2, (message_pos2))

        pygame.draw.rect(surface, BORDER_COLOR, border_top)
        pygame.draw.rect(surface, BORDER_COLOR, border_bottom)
        pygame.draw.rect(surface, BORDER_COLOR, border_center)
        pygame.draw.rect(surface, BORDER_COLOR, border_left)
        pygame.draw.rect(surface, BORDER_COLOR, border_right)

        pygame.draw.rect(surface, RACKET1_COLOR, racket1)
        pygame.draw.rect(surface, RACKET2_COLOR, racket2)

        pygame.draw.ellipse(surface, BALL_COLOR, ball)

        surface.blit(score1_show, (score1_pos))
        surface.blit(score2_show, (score2_pos))

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()