import pygame
import random as rd
import math
import numpy as np

class Star:
    def __init__(self, display):
        # Init. values
        self.display = display
        screen_height, screen_width = self.display.get_size()
        self.screen_centre = (screen_height/2, screen_width/2)
        self.max_draw_dist = math.sqrt(screen_height**2 + screen_width**2)/2

        # Init. positions and colours
        self.x, self.y = rd.randint(0, screen_width), rd.randint(0, screen_height)
        self.r, self.theta = convert_to_radians_from_centre(self.x, self.y, self.screen_centre)
        self.star_colour = (0,0,0)
        self.speed = 0 # TODO this should depend on self.r
        self.star_width = 1

    def draw(self):
        '''Draw star on surface.'''
        x = self.x
        y = self.y
        pygame.draw.ellipse(
            self.display, 
            self.star_colour, # star colour
            (x,y,self.star_width,self.star_width), # pygame.rect
            width=1) # star size

    def _update_position(self):
        # Redraw condition, if star pos. further away than dist. of diagonal
        if self.r < self.max_draw_dist:
            self.r = self.r*(1+self.speed) # increase r closer it gets to 
            self.star_width = self.star_width*(1.00001+self.speed) # and draw it larger
            self.speed += 0.000001
        else: # Redraw...
            self.__init__(self.display)
            # TODO is the below better?
            self.r = 0.5*self.r # redraw closer to centre

        self.x, self.y = convert_to_xy_from_top_left(
            self.r, 
            self.theta, 
            self.screen_centre)
        
    def _update_colour(self):
        scale_factor = (self.r/self.max_draw_dist)
        if max(self.star_colour) + 1 > 254:
            self.star_colour = (254,254,254)
        else:
            self.star_colour = (self.star_colour[0]+scale_factor,
                                self.star_colour[1]+scale_factor,
                                self.star_colour[2]+scale_factor)
            
    def _update_trail(self):
        current_star_pos = (self.x+self.star_width/2,self.y+self.star_width/2) 
        trail_start_pos = self.screen_centre # TODO should be a point somewhere along 
                                             # radius, and move as star does
        scale_factor = 0
        trail_width_size = 1
        trail_colour = (self.star_colour[0]*scale_factor,
                        self.star_colour[1]*scale_factor,
                        self.star_colour[2]*scale_factor)
        pygame.draw.line(
            self.display, 
            trail_colour, 
            current_star_pos,
            trail_start_pos, 
            trail_width_size)
        
    def update(self):
        '''Update star position, colour and it's trail'''
        self._update_position()
        self._update_colour()
        self._update_trail()
        self.draw()


def convert_to_radians_from_centre(x, y, centre):
    x_offset = x-centre[0]
    y_offset = y-centre[1]
    theta = math.atan2(x_offset, y_offset)
    r = math.sqrt(x_offset**2 + y_offset**2)
    return r, theta

def convert_to_xy_from_top_left(r, theta, centre):
    dx = r * math.cos(theta)
    dy = r * math.sin(theta)
    x = centre[0]+dx
    y = centre[1]+dy
    return x, y
