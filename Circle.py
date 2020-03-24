import math

import pygame

# Euclidean distance between two points
from Data import Data


def distance_between(pos1, pos2):
    # Gets x and y distance between points
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    
    # Returns distance via good ol Pythagoras
    return math.sqrt(dx ** 2 + dy ** 2)


def find_points_on_circumference(NUM_POINTS, radius):
    points_found = []
    
    for j in range(NUM_POINTS):
        # X and Y values of the points
        x = radius * math.sin((2 * math.pi / NUM_POINTS) * j) + Data.CENTER[0]
        y = radius * math.cos((2 * math.pi / NUM_POINTS) * j) + Data.CENTER[1]
        
        # Round points to nearest int and add as a tuple of new points on the circumference
        points_found.append(tuple(map(int, (x, y))))
    
    return points_found


class Circle:
    """This class represents a circle object.
    
    
    
    """
    
    def __init__(self, window, col, rad, thickness):
        self.window = window
        self.colour = col
        self.rad = rad
        self.thickness = thickness
        
        self.points_on_circumference = find_points_on_circumference(int(2 * math.pi * rad), rad)
    
    # Draws circle to window
    def draw(self):
        pygame.draw.circle(self.window, self.colour, Data.CENTER, self.rad, self.thickness)
    
    # Draws tangent line to the circle
    def draw_tangent_line(self, pos):
        x = pos[0] - Data.CENTER[0]
        y = pos[1] - Data.CENTER[1]
        
        if y == 0:
            pygame.draw.line(self.window, self.colour, (pos[0], pos[1] - 100), (pos[0], pos[1] + 100))
        
        else:
            slope = -x / y
            
            left_pos = (pos[0] - 100, pos[1] - 100 * slope)
            right_pos = (pos[0] + 100, pos[1] + 100 * slope)
            
            pygame.draw.line(self.window, self.colour, left_pos, right_pos)
    
    # Finds closest point to a position on the circumference of this circle
    def closest_point_on_circumference(self, position):
        
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
        
        # Returns closest point on circumference
        return closest
