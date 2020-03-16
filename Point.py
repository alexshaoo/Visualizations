import pygame


class Point:

    def __init__(self, name, rad, pos, col, window):
        self.name = name
        self.rad = rad
        self.pos = pos
        self.col = col
        self.window = window

    def draw(self):
        pygame.draw.circle(self.window, self.col, self.pos, self.rad)
