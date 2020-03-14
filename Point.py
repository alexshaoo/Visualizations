import pygame


class Point:

    def __init__(self, rad, pos, col, window):
        self.rad = rad
        self.pos = pos
        self.col = col
        self.window = window

    def draw(self):
        pygame.draw.circle(self.window, self.col, self.pos, self.rad)
