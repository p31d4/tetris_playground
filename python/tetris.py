#!/usr/bin/env python3

"""
A simple tetris game
"""

# import the pygame modules
import pygame
import numpy as np

# test if this is the file being executed
if __name__ == '__main__':

    pygame.init()             # initialize all imported pygame modules

    SCREEN_WIDTH       = 620  # define the screen width
    SCREEN_HEIGHT      = 620  # define the screen height
    GAME_SCREEN_WIDTH  = 300  # define the width of the area where the game will run
    GAME_SCREEN_HEIGHT = 600  # define the height of the area where the game will run

    # each block is supposed to be 30x30 pixels big, so in the tetris screen (300x600)
    # it is possible to put 10 blocks horizontally and 20 blocks vertically.

    # width and height are defined as 28 because 2 pixels are border
    WH = 28
    FLOOR = 580
    INITIAL_POSITION = np.array((120,-16))

    game_running = True

    # the colors used in the game:
    # [(black), (white), (a fancy yellow)]
    colors = [(0, 0, 0), (255, 255, 255), (204, 153, 0)]

    block = INITIAL_POSITION.copy()
    delta = np.array((0, 2))      # speed

    # initialize a window or screen for display (Surface)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
    pygame.display.set_caption('Tetris Game')    # set the current window caption
    screen.fill(colors[1])                       # fills the screen with white color

    # draws a rectangular shape on the screen.
    # in this case the thickness is defined to 5, this is a yellow border
    pygame.draw.rect(screen, colors[2], (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 5)
    pygame.display.flip()  # updates the whole display

    # game main loop
    while game_running:

        # move the block
        block += delta

        # if the block is on the floor, reset
        if block[1] > FLOOR:
            pygame.time.wait(1000)
            block[0], block[1] = INITIAL_POSITION[0], INITIAL_POSITION[1]

        # draws Tetris screen
        pygame.draw.rect(screen, colors[0], (10, 10, GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT))
        # draws block
        pygame.draw.rect(screen, colors[2], (block[0], block[1], WH, WH))
        # updates Tetris screen
        pygame.display.update(pygame.Rect(10, 10, GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT))

        for event in pygame.event.get():        # get events from the queue
            if event.type == pygame.QUIT:       # this event is triggered when the game is closed
                game_running = False

        pygame.time.wait(8)  # delay

    pygame.quit()       # uninitialize all pygame modules
