# imports
import pygame, sys
from pygame.locals import *

# imitialize pygame
pygame.init()

# assign FPS
FPS = 30
clock = pygame.time.Clock()

# setup colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# display dimensions
WIDTH = 300
HEIGHT = 300

# SETUP A 300X300 PIXEL DISPLAY 
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("my drawing")

# create lines and shapes
pygame.draw.line(DISPLAYSURF, BLUE, (150, 130), (130, 170))
pygame.draw.line(DISPLAYSURF, BLUE, (150, 130), (170, 170))
pygame.draw.line(DISPLAYSURF, GREEN, (130, 170), (170, 170))
pygame.draw.circle(DISPLAYSURF, BLACK, (100, 50), 30)



# game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # refresh screen
    pygame.display.update()
    clock.tick(FPS)