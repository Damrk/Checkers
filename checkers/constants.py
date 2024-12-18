import pygame

#board specs
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

#rgb colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (SQUARE_SIZE*0.44, SQUARE_SIZE*0.25))
