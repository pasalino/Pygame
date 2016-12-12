import pygame

class Board:
    BGCOLOR = (100, 50, 50)

    def __init__(self,name,windows_width,windows_height):
        self.windows_width = windows_width
        self.windows_height = windows_height
        self.name = name
        self.windowSurface = None


    def start(self):
        self.windowSurface = pygame.display.set_mode((self.windows_width, self.windows_height), 0, 32)
        self.windowSurface.fill(Board.BGCOLOR)
        pygame.display.set_caption(self.name)