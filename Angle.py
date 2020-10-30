import math

import pygame

from Data import Data


def get_positive_angle(angle_in_radians):
    """Returns the positive version of the angle measure (in radians)

    :arg angle_in_radians: The original angle measure, in radians, between -pi and pi

    :return: Corresponding ngle measure, in radians, between 0 and 2pi
    :rtype: float
    """
    if angle_in_radians < 0:
        return 2 * math.pi + angle_in_radians
    
    return angle_in_radians


def calculate_angle(pos):
    """Calculates the angle that a line formed by connecting a position to the center of the window makes with the x
    
    :param pos: The position of the starting point
    :return: The positive angle formed with this method
    :rtype: float
    """
    
    # Gets the different in x and y values between the points
    dy = Data.CENTER[1] - pos[1]
    dx = pos[0] - Data.CENTER[0]
    
    # Calculates the angle formed in the correct quadrant using the arctangent function
    angle = math.atan2(dy, dx)
    
    return get_positive_angle(angle)


def calculate_angle2(start, end):
    """Calculates the angle formed by a line and the positive axis. The line is formed by connecting two points
    
    :param start: The starting position
    :param end: The end point, which will be connected to the start point to form the line
    :return: The positive angle formed
    :rtype: float
    """
    
    # Gets positional difference between two points
    dy = start[1] - end[1]
    dx = end[0] - start[0]
    
    # Calculates the angle formed in the correct quadrant using the arctangent function
    angle = math.atan2(dy, dx)
    
    return get_positive_angle(angle)


class Angle:
    """This class represents an Angle object, whose main purpose is to store and do calculations involving angles
    
    :cvar radius: The radius of the portion circle which will be used to draw the angle
    """
    
    radius = Data.ARC_RADIUS
    
    def __init__(self, pos, colour, window, angle):
        """Create an angle object that
        
        :param pos: The position of the angle
        :param colour: The colour of the angle
        :param window: The surface that the angle will be drawn to
        :param angle: The angle value
        """
        
        # Starting, turning, and ending position
        self.pos = pos
        
        self.colour = colour
        
        self.window = window
        
        self.angle = angle
    
    # Draws arc sector angle ABC by connecting lines AB and BC (B is current point)
    def draw(self, A, C):
        """Draw the arc sector ABC, where B is the current point
        
        :param A: The starting postion
        :param C: The ending position
        :return: The angle formed by connecting the starting position, the current angle's position, and the ending
        position
        """
        
        # Rectangle arc will be inscribed in
        rect = pygame.Rect(self.pos[0] - self.radius, self.pos[1] - self.radius, 2 * self.radius, 2 * self.radius)
        
        # Gets angles of points that make up shape
        angleA = calculate_angle(A)
        angleB = calculate_angle(self.pos)
        angleC = calculate_angle(C)
        
        # Angle of lines AB and BC
        angleABO = calculate_angle2(self.pos, A)
        angleCBO = calculate_angle2(self.pos, C)
        
        # Checking and drawing angle
        if angleC < angleB < angleA or angleB < angleA < angleC or angleA < angleC < angleB:
            pygame.draw.arc(self.window, self.colour, rect, angleABO, angleCBO)
        
        elif angleC > angleB > angleA or angleB > angleA > angleC or angleA > angleC > angleB:
            pygame.draw.arc(self.window, self.colour, rect, angleCBO, angleABO)
    
    def to_degrees(self):
        """Converts the angle measure from radians to degrees
        
        :return: The current angle measure, in degrees
        """
    
        return self.angle * 180 // math.pi
