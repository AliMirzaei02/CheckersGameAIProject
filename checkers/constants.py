import pygame

WIDTH, HEIGHT = 700, 700
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# RGB colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)
BROWN = (64, 47, 29)
LIGHT_BROWN = (193, 154, 107)

CROWN = pygame.transform.scale(pygame.image.load('items/crown.png'), (WIDTH/10, HEIGHT/10))
TEXTURE = pygame.transform.scale(pygame.image.load('items/texture.png'), (WIDTH/10, HEIGHT/10))
