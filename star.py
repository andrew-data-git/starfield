import pygame as pg
import random as rd

class Star:

    def __init__(self, surface, width, height):
        self.surface = surface
        self.width = width
        self.height = height
        self.x = rd.randint(0, width)
        self.y = rd.randint(0, height)
        self.zoom = 1

    def update(self):
        self.zoom = self.zoom-1

    def show(self, star_colour):

        #

        # Remap the position
        dx = self.x * self.zoom + self.width/2
        dy = self.y * self.zoom + self.width/2
        #TODO make this work using polar coordinates, angle and radius
        #https://www.youtube.com/watch?v=qr4siL4Wktc&t=134s&ab_channel=CoderSpace

        # Draw the star
        rect = (dx, dy, 10, 10)
        pg.draw.ellipse(self.surface, star_colour, rect, width=5)

    def display_zoom(self):
        font = pg.font.Font('freesansbold.ttf', 32)
        text = font.render(str(self.zoom), True, (255,255,255))
        textRect = text.get_rect()
        textRect.center = (100,100)#(self.width // 2, self.height // 2)
        self.surface.blit(text, textRect)