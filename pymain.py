from SCC.board import Board
from SCC.helper import Direction
import sys

import pygame
from pygame.locals import *

board = Board()

board.make_move(40, 14)
board.make_move(0, 38)

size = (260, 310)

pygame.init()
screen = pygame.display.set_mode(size)
while 1:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    x = 0
    y = 0
    r = 10

    colors = [
        (128, 128, 128),
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (255, 0, 255),
        (255, 255, 0),
        (0, 255, 255)
    ]

    rows = [
        12,
        11,
        10,
        9,
        0,
        1,
        2,
        3,
        4,
        3,
        2,
        1,
        0,
        9,
        10,
        11,
        12,
    ]

    for h in board.get_hexes():
        pygame.draw.circle(screen,
                           colors[h.get_piece()],
                           (x * r*2 + r + r*rows[y],
                            y * (r-1)*2 + r),
                           r, r)

        if h.has_neighbour(Direction.RIGHT):
            x += 1
        else:
            y += 1
            x = 0

    pygame.display.update()
    pygame.time.delay(100)

    # print("Piece you want to move: ", end='')
    # id_from = int(input())
    # moves = board.get_moves(id_from)
    # print("Possible moves is ", moves)
    # print("Choose move: ", end='')
    # id_to = int(input())
    # board.make_move(id_from, id_to)
