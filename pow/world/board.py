import pygame

class Board:
    BGCOLOR = (100, 50, 50)

    def __init__(self,name,windows_width,windows_height):
        self.windows_width = windows_width
        self.windows_height = windows_height
        self.__windowSurface = pygame.display.set_mode((windows_width, windows_height), 0, 32)
        pygame.display.set_caption(name)

        self.__windowSurface.fill(Board.BGCOLOR)