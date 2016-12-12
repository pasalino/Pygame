import pygame
from pygame.locals import *
import sys
from world.board import Board
from pg.man import Man


name = "Gioco1"
width = 800
height = 600

board = Board(name,width,height)
player1 = Man(K_UP,K_DOWN,K_LEFT,K_RIGHT,K_RSHIFT)
player2 = Man(K_w,K_s,K_a,K_d,K_LSHIFT)


def main_loop():
    mainClock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    pygame.display.update()
    mainClock.tick(30)


def main():
    pygame.init()
    board.start()
    while True: main_loop()

if __name__ =="__main__":
    main()