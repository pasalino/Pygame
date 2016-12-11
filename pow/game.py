import pygame
from pygame.locals import *
import sys

def main():
    pygame.init()
    mainClock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ =="main":
    main()