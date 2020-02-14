import pygame
from pygame.locals import *
import sys

def main():

    pygame.init()
    pygame.display.set_mode((600, 600), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption('wawawa')

    (x, y) = (300, 300)
    (a, b) = (10, 50)

    while True:
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            x -= 1
        if pressed_key[K_RIGHT]:
            x += 1
        if pressed_key[K_UP]:
            y -= 1
        if pressed_key[K_DOWN]:
            y += 1

        pygame.display.update()
        pygame.time.wait(1)
        screen.fill((255, 255, 255, 255))

        #global a

        rect1 = pygame.draw.rect(screen, (0, 0, 255), (int(a), 10, int(b), 30), 0)
        circle1 = pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), 20)

        a += 0.3

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()