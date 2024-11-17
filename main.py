import random
import pygame
import numpy as np
from pygame.locals import *
import sys
from star import Star

# inspired by https://www.youtube.com/watch?v=17WoOqgXsRM&ab_channel=TheCodingTrain

# Initial conditions
WIDTH = 400
HEIGHT = 400
num_stars = 10

# Instantiate pygame
pygame.init()
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

# Create stars
stars = [None]*num_stars
for i, star in enumerate(stars):
    stars[i] = Star(DISPLAY, WIDTH, HEIGHT)

# Main Loop ---------------------------------------------------------------------
run = True
while run:
    # Draw --------------------------
    DISPLAY.fill((0,0,0))
    for star in stars:
        star.show()
        star.update()

    # Run ----------------------------
    pygame.display.flip()

    # Buttons ------------------------
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            pygame.quit()
            sys.exit()
