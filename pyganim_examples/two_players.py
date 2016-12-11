# test4_pyganim.py - A pyganim test program.
#
# This program shows off the use of a PygConductor to help organize your
# animation objects. Conductors basically let you call PygAnimation methods on
# several PygAnimation objects at once (e.g. You can have all the animation
# objects start playing at the same time.)
#
# The animation images come from POW Studios, and are available under an
# Attribution-only license. Check them out, they're really nice.
# http://powstudios.com/
#
# The walking sprites are shamelessly taken from the excellent SNES game
# Chrono Trigger.
# http://www.videogamesprites.net/ChronoTrigger


import pygame
from pygame.locals import *
import sys
import time
import pyganim

pygame.init()

# define some constants
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# set up the window
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Pyganim Test 4')

# load the "standing" sprites (these are single images, not animations)
front_standing = pygame.image.load('gameimages/crono_front.gif')
back_standing = pygame.image.load('gameimages/crono_back.gif')
left_standing = pygame.image.load('gameimages/crono_left.gif')
right_standing = pygame.transform.flip(left_standing, True, False)

playerWidth, playerHeight = front_standing.get_size()

# creating the PygAnimation objects for walking/running in all directions
animTypes = 'back_run back_walk front_run front_walk left_run left_walk'.split()
animObjs = {}
for animType in animTypes:
    imagesAndDurations = [('gameimages/crono_%s.%s.gif' % (animType, str(num).rjust(3, '0')), 0.1) for num in range(6)]
    animObjs[animType] = pyganim.PygAnimation(imagesAndDurations)

# create the right-facing sprites by copying and flipping the left-facing sprites
animObjs['right_walk'] = animObjs['left_walk'].getCopy()
animObjs['right_walk'].flip(True, False)
animObjs['right_walk'].makeTransformsPermanent()
animObjs['right_run'] = animObjs['left_run'].getCopy()
animObjs['right_run'].flip(True, False)
animObjs['right_run'].makeTransformsPermanent()

# have the animation objects managed by a conductor.
# With the conductor, we can call play() and stop() on all the animtion
# objects at the same time, so that way they'll always be in sync with each
# other.
moveConductor = pyganim.PygConductor(animObjs)

direction = DOWN # player starts off facing down (front)
direction2 = DOWN # player2

BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
WHITE = (255, 255, 255)
BGCOLOR = (100, 50, 50)

mainClock = pygame.time.Clock()
x = 300 # x and y are the player's position
y = 200

x2 = 200
y2 = 100

player1 = pygame.Rect(x,y,playerWidth,playerHeight);
player2 = pygame.Rect(x2,y2,playerWidth,playerHeight);


WALKRATE = 4
RUNRATE = 12


instructionSurf = BASICFONT.render('Arrow keys to move. Hold shift to run.', True, WHITE)
instructionRect = instructionSurf.get_rect()
instructionRect.bottomleft = (10, WINDOWHEIGHT - 10)

running = moveUp = moveDown = moveLeft = moveRight = False
running2 = moveUp2 = moveDown2 = moveLeft2 = moveRight2 = False


while True:

    windowSurface.fill(BGCOLOR)
    for event in pygame.event.get(): # event handling loop

        # handle ending the program

        if event.type == KEYDOWN:
            print(event.key)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == K_RSHIFT:
                # player has started running
                running = True

            if event.key == K_UP:
                moveUp = True
                moveDown = False
                if not moveLeft and not moveRight:
                    # only change the direction to up if the player wasn't moving left/right
                    direction = UP
            elif event.key == K_DOWN:
                moveDown = True
                moveUp = False
                if not moveLeft and not moveRight:
                    direction = DOWN
            elif event.key == K_LEFT:
                moveLeft = True
                moveRight = False
                if not moveUp and not moveDown:
                    direction = LEFT
            elif event.key == K_RIGHT:
                moveRight = True
                moveLeft = False
                if not moveUp and not moveDown:
                    direction = RIGHT

            # player 2

            if event.key == K_LSHIFT:
                # player has started running
                running2 = True

            if event.key == K_w:
                moveUp2 = True
                moveDown2 = False
                if not moveLeft2 and not moveRight2:
                    # only change the direction to up if the player wasn't moving left/right
                    direction2 = UP
            elif event.key == K_s:
                moveDown2 = True
                moveUp2 = False
                if not moveLeft2 and not moveRight2:
                    direction2 = DOWN
            elif event.key == K_a:
                moveLeft2 = True
                moveRight2 = False
                if not moveUp2 and not moveDown2:
                    direction2 = LEFT
            elif event.key == K_d:
                moveRight2 = True
                moveLeft2 = False
                if not moveUp2 and not moveDown2:
                    direction2 = RIGHT

        elif event.type == KEYUP:
            if event.key == K_RSHIFT:
                # player has stopped running
                running = False

            if event.key == K_UP:
                moveUp = False
                # if the player was moving in a sideways direction before, change the direction the player is facing.
                if moveLeft:
                    direction = LEFT
                if moveRight:
                    direction = RIGHT
            elif event.key == K_DOWN:
                moveDown = False
                if moveLeft:
                    direction = LEFT
                if moveRight:
                    direction = RIGHT
            elif event.key == K_LEFT:
                moveLeft = False
                if moveUp:
                    direction = UP
                if moveDown:
                    direction = DOWN
            elif event.key == K_RIGHT:
                moveRight = False
                if moveUp:
                    direction = UP
                if moveDown:
                    direction = DOWN


            if event.key == K_LSHIFT:
                # player has stopped running
                running2 = False

            if event.key == K_w:
                moveUp2 = False
                # if the player was moving in a sideways direction before, change the direction the player is facing.
                if moveLeft2:
                    direction2 = LEFT
                if moveRight2:
                    direction2 = RIGHT
            elif event.key == K_s:
                moveDown2 = False
                if moveLeft2:
                    direction2 = LEFT
                if moveRight2:
                    direction2 = RIGHT
            elif event.key == K_a:
                moveLeft2 = False
                if moveUp2:
                    direction2 = UP
                if moveDown2:
                    direction2 = DOWN
            elif event.key == K_d:
                moveRight2 = False
                if moveUp2:
                    direction2 = UP
                if moveDown2:
                    direction2 = DOWN

    if moveUp or moveDown or moveLeft or moveRight:
        if running:
            if direction == UP:
                animObjs['back_run'].blit(windowSurface, (x, y))
            elif direction == DOWN:
                animObjs['front_run'].blit(windowSurface, (x, y))
            elif direction == LEFT:
                animObjs['left_run'].blit(windowSurface, (x, y))
            elif direction == RIGHT:
                animObjs['right_run'].blit(windowSurface, (x, y))
        else:
            # walking
            if direction == UP:
                animObjs['back_walk'].blit(windowSurface, (x, y))
            elif direction == DOWN:
                animObjs['front_walk'].blit(windowSurface, (x, y))
            elif direction == LEFT:
                animObjs['left_walk'].blit(windowSurface, (x, y))
            elif direction == RIGHT:
                animObjs['right_walk'].blit(windowSurface, (x, y))


        # actually move the position of the player
        if running:
            rate = RUNRATE
        else:
            rate = WALKRATE

        if moveUp:
            y -= rate
        if moveDown:
            y += rate
        if moveLeft:
            x -= rate
        if moveRight:
            x += rate

    else:
        # standing still
        if direction == UP:
            windowSurface.blit(back_standing, (x, y))
        elif direction == DOWN:
            windowSurface.blit(front_standing, (x, y))
        elif direction == LEFT:
            windowSurface.blit(left_standing, (x, y))
        elif direction == RIGHT:
            windowSurface.blit(right_standing, (x, y))

    # make sure the player does move off the screen
    if x < 0:
        x = 0
    if x > WINDOWWIDTH - playerWidth:
        x = WINDOWWIDTH - playerWidth
    if y < 0:
        y = 0
    if y > WINDOWHEIGHT - playerHeight:
        y = WINDOWHEIGHT - playerHeight

    player1.x = x
    player1.y = y

    # player 2

    if moveUp2 or moveDown2 or moveLeft2 or moveRight2:
        # draw the correct walking/running sprite from the animation object
        if running2:
            if direction2 == UP:
                animObjs['back_run'].blit(windowSurface, (x2, y2))
            elif direction2 == DOWN:
                animObjs['front_run'].blit(windowSurface, (x2, y2))
            elif direction2 == LEFT:
                animObjs['left_run'].blit(windowSurface, (x2, y2))
            elif direction2 == RIGHT:
                animObjs['right_run'].blit(windowSurface, (x2, y2))
        else:
            # walking
            if direction2 == UP:
                animObjs['back_walk'].blit(windowSurface, (x2, y2))
            elif direction2 == DOWN:
                animObjs['front_walk'].blit(windowSurface, (x2, y2))
            elif direction2 == LEFT:
                animObjs['left_walk'].blit(windowSurface, (x2, y2))
            elif direction2 == RIGHT:
                animObjs['right_walk'].blit(windowSurface, (x2, y2))


        # actually move the position of the player
        if running2:
            rate2 = RUNRATE
        else:
            rate2 = WALKRATE

        if moveUp2:
            y2 -= rate2
        if moveDown2:
            y2 += rate2
        if moveLeft2:
            x2 -= rate2
        if moveRight2:
            x2 += rate2

    else:
        if direction2 == UP:
            windowSurface.blit(back_standing, (x2, y2))
        elif direction2 == DOWN:
            windowSurface.blit(front_standing, (x2, y2))
        elif direction2 == LEFT:
            windowSurface.blit(left_standing, (x2, y2))
        elif direction2 == RIGHT:
            windowSurface.blit(right_standing, (x2, y2))

    # make sure the player does move off the screen
    if x2 < 0:
        x2 = 0
    if x2 > WINDOWWIDTH - playerWidth:
        x2 = WINDOWWIDTH - playerWidth
    if y2 < 0:
        y2 = 0
    if y2 > WINDOWHEIGHT - playerHeight:
        y2 = WINDOWHEIGHT - playerHeight

    player2.x = x2
    player2.y = y2

    if moveUp2 or moveDown2 or moveLeft2 or moveRight2 or moveDown or moveUp or moveRight or moveLeft:
        moveConductor.play()  # calling play() while the animation objects are already playing is okay; in that case play() is a no-op
    else:
        moveConductor.stop()





    if player1.colliderect(player2):
        windowSurface.blit(instructionSurf, instructionRect)

    pygame.display.update()
    mainClock.tick(30) # Feel free to experiment with any FPS setting.