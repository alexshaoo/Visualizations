import math
import random

import pygame

from Button import Button
from Circle import Circle
from Data import Data
from Point import Point

# Initialize all modules necessary
pygame.init()

# Check for if pygame is running in main game loop
running = True

# Create window to draw on and its title
window = pygame.display.set_mode((Data.WIDTH, Data.HEIGHT))
pygame.display.set_caption(Data.TITLE)

# Initialize main circle object
circle = Circle(window, Data.WHITE, 200, Data.THICKNESS)

points = []

point_index = 0

# Buttons shown on screen
buttons = []
button_index = None

# Creates all buttons
# First button to trigger other buttons
buttons.append(Button((800, 0), (200, 100), "Theorems", Data.DARK_GREEN, Data.GREEN, True, window, Data.FONT, ""))

for j in range(5):
    b = Button((0, 100 * j), (200, 100), Data.theorem_names[j], Data.DARK_GREEN,
               Data.GREEN, False, window, Data.FONT, Data.descriptions[j])
    
    buttons.append(b)


# Finds point clicked on
def point_clicked_on(pos):
    # Checks every point
    for dot in points:
    
        # Returns index of point clicked on
        if abs(dot.pos[0] - pos[0]) <= Data.THICKNESS and abs(
                dot.pos[1] - pos[1]) <= Data.THICKNESS and dot.is_draggable:
            return points.index(dot)

    # If all points are searched and none are found, return index of original point that was selected
    return point_index


# If angles are on the same arc - for 4 angles it's sufficient to check alternating angles
def are_on_same_arc(angle1, angle2, angles):
    # Checks if indices are both even or odd, guarentee same arc
    return angles.index(angle1) % 2 == angles.index(angle2)


# Checks if a position is within the boundaries of a selectable box option
def within(top_left, size, pos):
    return top_left[0] <= pos[0] <= top_left[0] + size[0] and top_left[1] <= pos[1] <= top_left[1] + size[1]


# Function to readjust figure drawn onto circle
def construct(num_points, index):
    global points, point_index, button_index
    
    points = []
    Data.NUMBER_OF_POINTS = num_points
    point_index = 0
    button_index = index


def inscribed_angle():
    """Triggers inscribed angle default setup
    
    
    
    """
    
    construct(4, 1)
    
    for i in range(Data.NUMBER_OF_POINTS):
        
        # Names are the capital alphabet in order
        # Choose random location on the circumference of the circle
        if i == 2:
            points.append(Point(window, chr(i + 65), Data.CENTER, False))
        else:
            points.append(Point(window, chr(i + 65), random.choice(circle.points_on_circumference), True))


def cyclic_quadrilateral():
    """Makes cyclic quadrilateral
    
    """
    
    construct(4, 2)
    
    random_angles = []
    
    for i in range(Data.NUMBER_OF_POINTS):
        random_angles.append(random.uniform(0, 2 * math.pi))
    
    random_angles.sort()
    
    for i in range(Data.NUMBER_OF_POINTS):
        # Figure out corresponding point on circumference, given angle measure
        x = int(Data.CENTER[0] + circle.rad * math.cos(random_angles[i]))
        y = int(Data.CENTER[1] - circle.rad * math.sin(random_angles[i]))
        
        # Names are the capital alphabet in order
        # Choose random location on the circumference of the circle
        points.append(Point(window, chr(i + 65), (x, y), True))


def thales():
    """Makes right-angled semi-circle
    
    """
    construct(3, 3)
    
    random_location = random.choice(circle.points_on_circumference)
    points.append(Point(window, "A", random_location, False))
    
    points.append(Point(window, "B", random.choice(circle.points_on_circumference), True))
    
    points.append(Point(window, "C", (Data.CENTER[0] + (Data.CENTER[0] - random_location[0]),
                                      Data.CENTER[1] + (Data.CENTER[1] - random_location[1])), False))


def same_arc():
    """Makes a 4 sided shape consisting of angles formed by two lines extending from the same points

    """
    
    construct(4, 4)
    
    for i in range(Data.NUMBER_OF_POINTS):
        # Names are the capital alphabet in order
        # Choose random location on the circumference of the circle
        points.append(Point(window, chr(i + 65), random.choice(circle.points_on_circumference), True))
    
    # points.sort(key=maybe())


# Creates tangent line for theorem
def tangent():
    """Makes tangent line and connects it with the center of the circle
    
    """
    construct(2, 5)
    
    points.append(Point(window, "A", Data.CENTER, False))
    points.append(Point(window, "B", random.choice(circle.points_on_circumference), True))


def adjust_point(index, new_pos):
    points[index].pos = new_pos
    points[index].angle.pos = new_pos
    points[index].angle.angle = points[index].calculate_angle(Data.CENTER)


def get_positive_angle(angle_in_radians):
    if angle_in_radians < 0:
        return 2 * math.pi + angle_in_radians
    
    return angle_in_radians


# Draw function to draw everything onto the window
def draw():
    # Draws big circle
    circle.draw()
    
    # Draw buttons to canvas
    for button in buttons:
        button.draw()
    
    for index, point in enumerate(points):
        point.draw()
        
        # Calculates angle between each point and center of circle
        point.calculate_angle(Data.CENTER)
        
        # Draw a line between each adjacent pair of points
        point.draw_line(points[index - 1], Data.RED)
        
        point.angle.draw(points[index - 1].pos, points[(index + 1) % Data.NUMBER_OF_POINTS].pos)
    
    if button_index is not None:
        
        buttons[button_index].show_description()
        
        if button_index == 5:
            circle.draw_tangent_line(points[1].pos)
    
    # Highlight selected point by drawing over top with a yellow circle
    if len(points) > 0:
        pygame.draw.circle(window, Data.YELLOW, points[point_index].pos, Data.THICKNESS)


# Main loop
while running:
    
    for event in pygame.event.get():
        
        # Quits game
        if event.type == pygame.QUIT:
            running = False
        
        # If mouse is moving and left click is selected, dragging point across
        elif event.type == pygame.MOUSEMOTION and event.buttons[0] and len(points) > 0:
            
            # Get position of mouse
            position = pygame.mouse.get_pos()
            
            # Finds index of point clicked on
            point_index = point_clicked_on(position)
            
            # Sets new selected point, and position of that point to the new position on the circumference
            if points[point_index].is_draggable:
                points[point_index].pos = circle.closest_point_on_circumference(position)
            
            adjust_point(point_index, points[point_index].pos)
        
        # If left mouse button is clicked
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            # Gets position of mouse
            position = pygame.mouse.get_pos()
            
            # If the theorem button is selected
            if within(buttons[0].pos, buttons[0].size, position):
                for button in buttons[1:]:
                    button.is_shown = not button.is_shown
            
            # Construct an scrinbed angle
            elif within(buttons[1].pos, buttons[1].size, position):
                
                inscribed_angle()
            
            # Construct a cyclic quadrilateral
            elif within(buttons[2].pos, buttons[2].size, position):
                
                cyclic_quadrilateral()
            
            # Make triangle with one edge as diameter
            elif within(buttons[3].pos, buttons[3].size, position):
                
                thales()
            
            # Makes a
            elif within(buttons[4].pos, buttons[4].size, position):
                
                same_arc()
            
            # Makes tangent line
            elif within(buttons[5].pos, buttons[5].size, position):
                
                tangent()
                
                circle.draw_tangent_line(points[point_index].pos)
    
    # Repaints over the surface with black
    window.fill(Data.BLACK)
    
    # Draws everything to the window
    draw()
    
    # Updates display drawn
    pygame.display.update()
