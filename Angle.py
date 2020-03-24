import math

import pygame

# Converts an angle measure to its positive variant
from Data import Data


def get_positive_angle(angle_in_radians):
    if angle_in_radians < 0:
        return 2 * math.pi + angle_in_radians
    
    return angle_in_radians


# Calculates angle formed by 1 point and the origin
def calculate_angle(pos):
    dy = Data.CENTER[1] - pos[1]
    dx = pos[0] - Data.CENTER[0]
    
    angle = math.atan2(dy, dx)
    
    return get_positive_angle(angle)


# Calculates angle formed by 2 points
def calculate_angle2(start, end):
    dy = start[1] - end[1]
    dx = end[0] - start[0]
    
    angle = math.atan2(dy, dx)
    
    return get_positive_angle(angle)


class Angle:
    radius = 25
    
    def __init__(self, pos, colour, window, angle):
        
        # Starting, turning, and ending position
        self.pos = pos
        
        self.colour = colour
        
        self.window = window
        
        self.angle = angle
    
    # Draws arc sector angle ABC by connecting lines AB and BC (B is current point)
    def draw(self, A, C):
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
    
    # Converts angle measurement from radians to degrees
    def to_degrees(self):
        
        # Gets rounded angle
        return self.angle * 180 // math.pi
