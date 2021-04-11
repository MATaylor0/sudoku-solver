import pygame
from pygame.locals import *
from solver import *

pygame.init()

HEIGHT = 540
WIDTH = 600

def main():
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Sudoku')
    # board = Grid(9, 9, WIDTH, HEIGHT, window)
    # key = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    # redrawWindow(window, board)
    pygame.display.update()

    pass

if __name__ == '__main__':
    main()