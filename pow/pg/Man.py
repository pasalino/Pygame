import pygame
import pyganim

class Man:
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    WALKRATE = 4
    RUNRATE = 12

    def __init__(self,up_key,bottom_key,left_key,right_key,run_key):
        self.x_pos = 0
        self.y_pos = 0
        self.__up_key = up_key
        self.__bottom_key = bottom_key
        self.__left_key = left_key
        self.__right_key = right_key
        self.__run_key = run_key

        self.__front_standing = pygame.image.load('gameimages/crono_front.gif')
        self.__back_standing = pygame.image.load('gameimages/crono_back.gif')
        self.__left_standing = pygame.image.load('gameimages/crono_left.gif')
        self.__right_standing = pygame.transform.flip(self.__left_standing, True, False)

        self.__playerWidth, self.__playerHeight = self.front_standing.get_size()

        # creating the PygAnimation objects for walking/running in all directions
        animTypes = 'back_run back_walk front_run front_walk left_run left_walk'.split()
        self.__animObjs = {}
        for animType in animTypes:
            imagesAndDurations = [('gameimages/crono_%s.%s.gif' % (animType, str(num).rjust(3, '0')), 0.1) for num in range(6)]
            self.animObjs[animType] = pyganim.PygAnimation(imagesAndDurations)

        # create the right-facing sprites by copying and flipping the left-facing sprites
        self.__animObjs['right_walk'] = self.__animObjs['left_walk'].getCopy()
        self.__animObjs['right_walk'].flip(True, False)
        self.__animObjs['right_walk'].makeTransformsPermanent()
        self.__animObjs['right_run'] = self.__animObjs['left_run'].getCopy()
        self.__animObjs['right_run'].flip(True, False)
        self.__animObjs['right_run'].makeTransformsPermanent()

        self.__moveConductor = pyganim.PygConductor(self.__animObjs)

        self.__direction = Man.DOWN
        self.__area = pygame.Rect(self.x_pos,self.y_pos,self.__playerWidth,self.__playerHeight)

        self.__running = self.__moveUp = self.__moveDown = self.__moveLeft = self.__moveRight = False

