import random
import pygame as pg
import numpy as np
from pygame.locals import *
import sys
from star import Star

# inspired by https://www.youtube.com/watch?v=17WoOqgXsRM&ab_channel=TheCodingTrain

# Initial conditions
WIDTH = 800
HEIGHT = 800
screen_colour = (0, 0, 0)
star_colour = (255, 255, 255)
num_stars = 50
max_zoom = 100

# Instantiate pygame
pg.init()
window = pg.display.set_mode((WIDTH, HEIGHT))
main_clock = pg.time.Clock()

# Create stars
stars = [None]*num_stars
for i, star in enumerate(stars):
    stars[i] = Star(window, WIDTH, HEIGHT)

# Main Loop ---------------------------------------------------------------------
run = True
while run:
    # Draw --------------------------
    window.fill(screen_colour)
    for star in stars:
        star.update()
        star.show(star_colour)
    stars[0].display_zoom()

    # Run ----------------------------
    pg.display.update()
    main_clock.tick(1)

    # Buttons ------------------------
    for event in pg.event.get():
        if event.type == MOUSEBUTTONDOWN:
            pg.quit()
            sys.exit()
