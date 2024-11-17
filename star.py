import pygame
import random as rd
import math
import numpy as np

class Star:
    def __init__(self, display, screen_width, screen_height):
        # Init. values
        self.star_rect = None
        self.star_width = 10
        self.surface = display
        self.screen_centre = (screen_width/2, screen_height/2)

        # Star positions
        self.x, self.y = rd.randint(0, screen_width), rd.randint(0, screen_height)
        self.r, self.theta = convert_to_radians_from_centre(self.x, self.y, self.screen_centre)

    def show(self):
        '''Draw star on surface.'''
        x = self.x
        y = self.y
        pygame.draw.ellipse(
            self.surface, 
            (255,255,255), # star colour
            (x,y,self.star_width,self.star_width), # pygame.rect
            width=self.star_width) # star size

    def update(self):
        ''''''
        if self.r < 200:
            self.r = self.r + 0.05
        else:
            self.x = rd.randint(0, self.screen_centre[0])
            self.y = rd.randint(0, self.screen_centre[1])
            self.r, self.theta = convert_to_radians_from_centre(
                self.x, self.y, self.screen_centre)

        self.x, self.y = convert_to_xy_from_top_left(
            self.r, 
            self.theta, 
            self.screen_centre)

        pygame.draw.line(
            self.surface, 
            (255,0,0), 
            self.screen_centre, 
            (self.x+self.star_width/2,self.y+self.star_width/2), 
            width=2)


def convert_to_radians_from_centre(x, y, centre):
    ''''''
    x_offset = x-centre[0]
    y_offset = y-centre[1]
    theta = math.atan2(x_offset, y_offset)
    r = math.sqrt(x_offset**2 + y_offset**2)
    return r, theta

def convert_to_xy_from_top_left(r, theta, centre):
    ''''''
    dx = r * math.cos(theta)
    dy = r * math.sin(theta)
    x = centre[0]+dx
    y = centre[1]+dy
    return x, y
