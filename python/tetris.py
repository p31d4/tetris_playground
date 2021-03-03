#!/usr/bin/env python3

"""
A simple tetris game
"""

# import the pygame modules
import pygame

# test if this is the file being executed
if __name__ == '__main__':

    pygame.init()             # initialize all imported pygame modules

    SCREEN_WIDTH       = 620  # define the screen width
    SCREEN_HEIGHT      = 620  # define the screen height
    GAME_SCREEN_WIDTH  = 300  # define the width of the area where the game will run
    GAME_SCREEN_HEIGHT = 600  # define the height of the area where the game will run

    game_running = True

    # the colors used in the game:
    # [(black), (white), (a fancy yellow)]
    colors = [(0, 0, 0), (255, 255, 255), (204, 153, 0)]

    # initialize a window or screen for display (Surface)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Tetris Game')    # set the current window caption
    screen.fill(colors[1])                       # fills the screen with white color

    # draws a rectangular shape on the screen.
    # In this case the thickness is defined to 5, this is a yellow border
    pygame.draw.rect(screen, colors[2], (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 5)

    # game main loop
    while game_running:
        # draw the game screen over the main screen
        pygame.draw.rect(screen, colors[0], (10, 10, GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT))

        pygame.display.update()  # updates the entire Surface area because no argument was passed

        for event in pygame.event.get():        # get events from the queue
            if event.type == pygame.QUIT:       # this event is triggered when the game is closed
                game_running = False

    pygame.quit()       # uninitialize all pygame modules
