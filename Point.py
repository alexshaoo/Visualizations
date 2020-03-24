import math

import pygame


class Point:

    def __init__(self, name, rad, pos, col, angle):
        self.name = name
        self.rad = rad
        self.pos = pos
        self.col = col

        # Angle between point and center of circle
        self.angle = angle

    # Draws line between itself and another point
    def draw_line(self, point, window, colour):
        pygame.draw.line(window, colour, self.pos, point.pos)

    # Draws itself to canvas
    def draw(self, window):
        pygame.draw.circle(window, self.col, self.pos, self.rad)

    # Calculates angle between point, with reference any other point
    def calculate_angle(self, reference_point):
        dx = self.pos[0] - reference_point[0]
        dy = reference_point[1] - self.pos[1]

        angle = math.atan2(dy, dx)

        # Returns positive angle
        if angle < 0:
            self.angle = 2 * math.pi + angle
            return 2 * math.pi + angle
        self.angle = angle
        return angle

    # Draws the point's name onto the window
    def display_name(self, window):
        pass
