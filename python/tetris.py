#!/usr/bin/env python3

"""
A simple Tetris game
"""

# import the pygame modules
import pygame
import numpy as np

class ScreenPiece:
    """
        This class defines a Tetris piece.
        It is composed by four fundamental blocks arranged in diferent ways (shapes).
        Each block is supposed to be 30x30 pixels big, so in the Tetris screen (300x600)
        it is possible to put 10 blocks horizontally and 20 blocks vertically.
        Only one instance of this piece is required, because at any given time,
        there will be just one piece running through the screen.
    """

    def __init__(self, _screen, color):
        self.screen = _screen
        self.color = color
        self.on_the_floor = False
        self.blocks = [np.array((0,0)) for idx in range(4)]

    def reshape(self, shape, offset):
        """
            There will be always just one piece falling through the screen.
            Every time the piece hits the ground it will be moved to the top
            again e reshaped to have a random new shape (could be the same old)
        """
        for idx in range(4):
            self.blocks[idx][0] = shape[idx][0] * 30 + offset[0]
            self.blocks[idx][1] = shape[idx][1] * 30 + offset[1]

    def draw_piece(self):
        """
            draw all the four fundamental blocks
        """
        for idx in range(4):
            pygame.draw.rect(screen, self.color,
                             (self.blocks[idx][0] + 1, self.blocks[idx][1] + 1,
                              BLOCK_WH - 2, BLOCK_WH - 2))

    def move(self, _delta):
        """
            move the piece on the screen at a "_delta" rate
        """
        for idx in range(4):
            if self.blocks[idx][1] >= FLOOR:
                pygame.time.wait(1000)
                self.reshape(SHAPES[0], OFFSETS[0])
                break
            self.blocks[idx] += _delta


# test if this is the file being executed
if __name__ == '__main__':

    pygame.init()             # initialize all imported pygame modules

    SCREEN_WH          = 620  # define the screen width and height
    GAME_SCREEN_WIDTH  = 300  # define the width of the area where the game will run
    GAME_SCREEN_HEIGHT = 600  # define the height of the area where the game will run

    BLOCK_WH = 30
    SHAPES = [np.array(((0,0), (0,-1), (1,-1), (1,0)))]
    # y offsite is one Block, 10 means the offset of the Tetris screen
    OFFSETS = [np.array((120, 10 - BLOCK_WH))]
    FLOOR = 2 * GAME_SCREEN_HEIGHT - SCREEN_WH

    game_running = True

    # the colors used in the game:
    # [(black), (white), (a fancy yellow)]
    colors = [(0, 0, 0), (255, 255, 255), (204, 153, 0)]

    # initialize a window or screen for display (Surface)
    screen = pygame.display.set_mode((SCREEN_WH, SCREEN_WH), pygame.DOUBLEBUF)
    pygame.display.set_caption('Tetris Game')    # set the current window caption
    screen.fill(colors[1])                       # fills the screen with white color

    screen_piece = ScreenPiece(screen, colors[2])
    screen_piece.reshape(SHAPES[0], OFFSETS[0])

    # draws a rectangular shape on the screen.
    # in this case the thickness is defined to 5, this is a yellow border
    pygame.draw.rect(screen, colors[2], (0, 0, SCREEN_WH, SCREEN_WH), 5)
    pygame.display.flip()  # updates the whole display

    delta = np.array((0, 30))

    # game main loop
    while game_running:
        # draws Tetris screen
        pygame.draw.rect(screen, colors[0], (10, 10, GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT))
        screen_piece.move(delta)
        screen_piece.draw_piece()
        # updates Tetris screen
        pygame.display.update(pygame.Rect(10, 10, GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT))

        for event in pygame.event.get():        # get events from the queue
            if event.type == pygame.QUIT:       # this event is triggered when the game is closed
                game_running = False

        pygame.time.wait(500)  # delay

    pygame.quit()       # uninitialize all pygame modules
