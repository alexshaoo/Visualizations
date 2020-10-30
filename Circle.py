import math

import pygame

from Data import Data


# Euclidean distance between two points
def distance_between(pos1, pos2):
    """Calculates the Euclidean distance between two positions
    
    :arg pos1: The first position
    :arg pos2: The second position
    
    :return: The distance between the two positions
    :rtype: float
    """
    
    # Gets x and y distance between points
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    
    # Returns distance via good ol Pythagoras
    return math.sqrt(dx ** 2 + dy ** 2)


def find_points_on_circumference(NUM_POINTS, radius):
    """Find all the points on the circumference of a given circle
    
    :arg NUM_POINTS: A constant multiple which determines how many points should be found
    :arg radius: The radius of the given circle, whose positions on the circumference
    
    :return: A list of the points on the circumference of the circle, specified by the radius, which have been found
    :rtype: List
    """
    
    points_found = []
    
    for j in range(NUM_POINTS):
        # X and Y values of the points
        x = radius * math.sin((2 * math.pi / NUM_POINTS) * j) + Data.CENTER[0]
        y = radius * math.cos((2 * math.pi / NUM_POINTS) * j) + Data.CENTER[1]
        
        # Round points to nearest int and add as a tuple of new points on the circumference
        points_found.append(tuple(map(int, (x, y))))
    
    return points_found


class Circle:
    """This class represents circles. Need I say more?"""
    
    def __init__(self, window, col, rad, thickness):
        """Creates a new circle object
        
        :arg window: The window onto which the circle will be drawn on
        :arg col: The colour of the circle
        :arg rad: The radius of the circle
        :arg thickness: The thickness of the circle's circumference
        """
        self.window = window
        self.colour = col
        self.rad = rad
        self.thickness = thickness
        
        # The points on the circle's circumference
        self.points_on_circumference = find_points_on_circumference(int(2 * math.pi * rad), rad)
    
    def draw(self):
        """Draws the circle itself to the window
        """
        
        pygame.draw.circle(self.window, self.colour, Data.CENTER, self.rad, self.thickness)
    
    def draw_tangent_line(self, pos):
        """Draws the tangent line to the circle at a given position
        
        :arg pos: A position on the circle's circumference
        """
        
        # Get the x and y values, relative to the center of the circle, of the position
        x = pos[0] - Data.CENTER[0]
        y = pos[1] - Data.CENTER[1]
        
        # Check for undefined slope, draw a vertical line in this case
        if y == 0:
            pygame.draw.line(self.window, self.colour, (pos[0], pos[1] - 100), (pos[0], pos[1] + 100))
        
        else:
            
            # Gets the slope (derived using derivative calculus :DD)
            slope = -x / y
            
            # The positions of the points to the left and right of the position, which will be used to form the line
            left_pos = (pos[0] - 100, pos[1] - 100 * slope)
            right_pos = (pos[0] + 100, pos[1] + 100 * slope)
            
            # Draws the line by connecting said points
            pygame.draw.line(self.window, self.colour, left_pos, right_pos)
    
    # Finds closest point to a position on the circumference of this circle
    def closest_point_on_circumference(self, position):
        
        """Finds the closest point on the circumference of the circle, given a position
        
        :arg position: The position, which doesn't necessarily have to be on the circle's circumference
        
        :return: The location of the closest point on the circle's circumference
        :rtype: tuple
        """
        
        # Default closest point to first point on circumference
        closest = self.points_on_circumference[0]
        shortest_distance = distance_between(Data.CENTER, closest)
        
        # Checks each dot on the circumference
        for dot in self.points_on_circumference:
            
            # Find distance between point and the position
            distance = distance_between(position, dot)
            
            # Sets new closest point and distance if a closer point is found
            if distance < shortest_distance:
                closest = dot
                shortest_distance = distance
        
        # Once all points have been checked, return the closest point on circumference
        return closest
