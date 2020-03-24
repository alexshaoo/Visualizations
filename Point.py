import math

import pygame

from Angle import Angle
from Circle import Circle
from Data import Data


class Point(Circle):
    # Static class variables
    rad = 10
    
    BLUE = Data.BLUE
    
    PURPLE = Data.PURPLE
    
    def __init__(self, window, name, pos, is_draggable):
        super().__init__(window, Point.BLUE, self.rad, 1)
        self.pos = pos
        self.name = name
        self.col = Point.BLUE
        self.is_draggable = is_draggable
        
        # Angle between point and center of circle
        self.angle = Angle(pos, Point.PURPLE, self.window, self.calculate_angle(Data.CENTER))
    
    # Draws line between itself and another point
    def draw_line(self, point, colour):
        pygame.draw.line(self.window, colour, self.pos, point.pos)
    
    # Draws itself to canvas
    def draw(self):
        pygame.draw.circle(self.window, self.col, self.pos, self.rad)
    
    # Calculates angle between a line created by connecting point to origin and the positive x axis
    def calculate_angle(self, origin):
        # Horizontal difference between starting and end point
        dx = self.pos[0] - origin[0]
        
        # Flipped because positive y direction is down
        dy = origin[1] - self.pos[1]
        
        return math.atan2(dy, dx)
    
    # Returns angle value
    def return_angle(self):
        return self.angle.angle
    
    # Draws the point's name onto the window
    def display_name(self, window):
        pass
