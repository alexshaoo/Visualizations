import math

import pygame

from Angle import Angle
from Circle import Circle
from Data import Data


class Point(Circle):
    """A class which represents a point. It inherits from the Circle class, as a point is a circle
    
    :cvar rad: The radii of all points are 10
    """
    
    rad = 10
    
    def __init__(self, window, name, pos, is_draggable):
        """Construct a new circle with the given parameters, as well as initalize others that were sent in
        
        :arg window: The surface upon which the shapes will be drawn
        :arg name: The name of the specified point
        :arg pos: The position of the point
        :arg is_draggable: Whether or not a point can be selected, or moved accordingly
        """
        
        super().__init__(window, Data.BLUE, self.rad, 1)
        self.pos = pos
        self.name = name
        self.col = Data.BLUE
        self.is_draggable = is_draggable
        
        # Angle between point and center of circle - Useful for navigating using polar coordinates
        self.angle = Angle(pos, Data.PURPLE, self.window, self.calculate_angle(Data.CENTER))
    
    def draw_line(self, point, colour):
        """Draws a line between itself and another point
        
        :param point: Other point to connect the line to
        :param colour: The colour of the line to be formed
        :return:
        """
        
        pygame.draw.line(self.window, colour, self.pos, point.pos)
    
    def draw(self):
        """Draws itself to the canvas
        
        :return:
        """
        pygame.draw.circle(self.window, self.col, self.pos, self.rad)
    
    def calculate_angle(self, origin):
        """Calculates the angle between a line created by connecting point to origin with the positive x-axis
        
        :param origin: The reference point, also the origin of the main circle
        :return: The angle measure (in radians) of the angle formed in this process
        :rtype: float
        """
        # Horizontal difference between starting and end point
        dx = self.pos[0] - origin[0]
        
        # Flipped because positive y direction is down
        dy = origin[1] - self.pos[1]
        
        return math.atan2(dy, dx)
    
    # Returns angle value
    def return_angle(self):
        """Returns the angle value of a point
        
        :return: The angle position of the point
        """
        return self.angle.angle
