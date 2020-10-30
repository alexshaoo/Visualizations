import math
import random

import pygame

from Button import Button
from Circle import Circle
from Data import Data
from Point import Point

"""This is the Circle Theorems.py file, which uses pygame to create an interactive visual version of multiple circle
theorems. Creates and uses buttons to navigate to different theorems, and uses the Data, Circle, Point, Angle, and
Button classes to illustrate various theorems based off of the central idea of having inscribed angles in a circle.

author: alexs

"""

# Initialize all pygame modules necessary
pygame.init()

# Check for if pygame is running in main game loop
running = True

# Create window to draw on and set its title
window = pygame.display.set_mode((Data.WIDTH, Data.HEIGHT))
pygame.display.set_caption(Data.TITLE)

# Initialize main circle object
circle = Circle(window, Data.WHITE, 200, Data.THICKNESS)

# List of points and the index of the point that's currently selected
points = []
point_index = 0

# Buttons shown on screen
buttons = []
button_index = None

# First button to trigger other buttons to appear
buttons.append(Button((800, 0), (200, 100), "Theorems", Data.DARK_GREEN, Data.GREEN, True, window, Data.FONT, ""))

# Creates the buttons specific to each theorem
for j in range(5):
    b = Button((0, 100 * j), (200, 100), Data.theorem_names[j], Data.DARK_GREEN,
               Data.GREEN, False, window, Data.FONT, Data.descriptions[j])
    
    buttons.append(b)


# Checks if a position is within the boundaries of a selectable box option
def within(top_left, size, pos):
    """Checks if a position is within the boundaries of a rectangle
    
    :arg top_left: A tuple containing the position of the top left of the rectangle
    :arg size: Another tuple containing the size of the rectangle
    :arg pos: Yet another tuple, which stores a position that is to be checked
    
    :returns: A boolean which states whether the position is within the specified boundaries
    :rtype: boolean
    """
    return top_left[0] <= pos[0] <= top_left[0] + size[0] and top_left[1] <= pos[1] <= top_left[1] + size[1]


def point_clicked_on(pos):
    """Finds the index of the point that the user has selected via mouse click
    
    :arg pos: The position of the mouse click
    
    :returns: The index of the new point that was selected, otherwise return the index of the point that
    was previously selected, as no new selection was made
    :rtype: int
    """
    for dot in points:
        
        # Returns index of point clicked on
        if abs(dot.pos[0] - pos[0]) <= Data.THICKNESS and abs(
                dot.pos[1] - pos[1]) <= Data.THICKNESS and dot.is_draggable:
            return points.index(dot)
    
    # If all points are searched and none are found, return index of original point that was selected
    return point_index


def new_shape_readjustments(num_points, index):
    """Adjusts global constants when making a new shape for a theorem
    
    :arg num_points: The number of points that the new shape needs to be formed from
    :arg index: The index of the button that was selected
    """
    
    global points, point_index, button_index
    
    # Empties out current points
    points = []
    
    Data.NUMBER_OF_POINTS = num_points
    
    # Defaults the index of the selected point to the first one
    point_index = 0
    
    button_index = index


def adjust_point(index, new_pos):
    """Adjusts the attributes of the selected point
    :arg index: The index of the selected point
    :arg new_pos: The new position that the selected point is being dragged (or moved in some way) to
    """
    points[index].pos = new_pos
    points[index].angle.pos = new_pos
    points[index].angle.angle = points[index].calculate_angle(Data.CENTER)


def get_position_on_circle_from_angle(angle_in_radians):
    """Given an angle measure in radians, this function gets the corresponding position of the point on the circle
    
    :param angle_in_radians: The angle measure component, in radians, of the polar coordinate of a point
    :return: The position of the point
    """
    
    # Figure out corresponding point on circumference, given an angle measure
    x = int(Data.CENTER[0] + circle.rad * math.cos(angle_in_radians))
    y = int(Data.CENTER[1] - circle.rad * math.sin(angle_in_radians))
    
    return x, y


def inscribed_angle():
    """Creates inscribed angle default setup - Two points on the circumference, both of which are connected to a third
    point on the circumference as well as the center of the circle
    """
    
    # 4 points, button number 1
    new_shape_readjustments(4, 1)
    
    positions = sorted([random.choice(circle.points_on_circumference) for i in range(3)])
    
    for i in range(Data.NUMBER_OF_POINTS):
        
        # Names of buttons are the capital letters starting from A
        if i == 2:
            
            # Point at the center
            points.append(Point(window, chr(i + 65), Data.CENTER, False))
        
        # Chooses random locations on the circumference in a certain order, to create an inscribed angle
        elif i < 2:
            points.append(Point(window, chr(i + 65), positions[i], True))
        
        else:
            points.append(Point(window, chr(i + 65), positions[i - 1], True))


def cyclic_quadrilateral():
    """Makes cyclic quadrilateral - A 4 sided shape whose vertices lie on the circumference of the circle. The lines
    that are formed by connecting each pair of adjacent points cannot intersect any other lines
    """
    
    # 4 points, button number 2
    new_shape_readjustments(4, 2)
    
    random_angles = []
    
    # Chooses random angles with which to select points from
    for i in range(Data.NUMBER_OF_POINTS):
        random_angles.append(random.uniform(0, 2 * math.pi))
    
    # Sorts them in increasing order
    random_angles.sort()
    
    positions = [get_position_on_circle_from_angle(random_angle) for random_angle in random_angles]
    
    for i in range(Data.NUMBER_OF_POINTS):
        # Creates a draggable point at that specific position
        points.append(Point(window, chr(i + 65), positions[i], True))


def thales():
    """Makes triangle which has a leg that is the diameter of the circle - Consisting of two points which are
    diametrically opposite to each other and another random point on the circumference
    """
    
    # Three points, button number 3
    new_shape_readjustments(3, 3)
    
    # Chooses a random location for the first point
    random_location = random.choice(circle.points_on_circumference)
    
    # Creates a point at that location
    points.append(Point(window, "A", random_location, False))
    
    # Creates a point at another random position
    points.append(Point(window, "B", random.choice(circle.points_on_circumference), True))
    
    # Using the random position, construct a point which is on the opposite side of the circle
    points.append(Point(window, "C", (Data.CENTER[0] + (Data.CENTER[0] - random_location[0]),
                                      Data.CENTER[1] + (Data.CENTER[1] - random_location[1])), False))


def same_arc():
    """Makes a 4 sided shape consisting of angles formed by two lines extending from the same points - There must be
    exactly one overlap between the points, as we constuct three points and then construct a fourth by connecting two
    of the points' arcs to another random location on the circle
    """
    
    # 4 points, button number 4
    new_shape_readjustments(4, 4)
    
    random_angles = []
    
    # Chooses random angles with which to select points from
    for i in range(Data.NUMBER_OF_POINTS):
        random_angles.append(random.uniform(0, 2 * math.pi))
    
    # Sorts them in increasing order
    random_angles.sort()
    
    # Order that the points will be connected in - given using indices
    angle_order = (0, 2, 1, 3)
    
    for i in range(Data.NUMBER_OF_POINTS):
        # Creates a draggable point at that specific position
        points.append(
            Point(window, chr(i + 65), get_position_on_circle_from_angle(random_angles[angle_order[i]]), True))


# Creates tangent line for theorem
def tangent():
    """Chooses a random point on the circle, constructs a tangent line, and connects it with the center of the circle
    """
    
    # Two points necessary, button number 5
    new_shape_readjustments(2, 5)
    
    # First point is the center of the circle
    points.append(Point(window, "A", Data.CENTER, False))
    
    # Chooses a random point on the circumference for the second
    points.append(Point(window, "B", random.choice(circle.points_on_circumference), True))


def draw():
    """Function which draws all shapes onto the window. First draws the circle, and then each button which should be
    shown, as well as each point and lines and angles that relate to them. Also shows the description of each theorem
    based on the button that was selected
    """
    
    # Draws main circle
    circle.draw()
    
    # Draw each button to the canvas
    for button in buttons:
        button.draw()
    
    # Draws each point
    for index, point in enumerate(points):
        point.draw()
        
        # Recalculates angle between each point and center of circle
        point.calculate_angle(Data.CENTER)
        
        # Draw a line to connect each adjacent pair of points
        point.draw_line(points[index - 1], Data.RED)
        
        # Draw an angle formed between three adjacent points
        point.angle.draw(points[index - 1].pos, points[(index + 1) % Data.NUMBER_OF_POINTS].pos)
    
    # Shows the description of the button, given the index of the button that was selected
    if button_index is not None:
    
        buttons[button_index].show_description()
    
        # Draws a tangent line for the sepcific button which is concerned with tangent lines
        if button_index == 5:
            circle.draw_tangent_line(points[1].pos)
    
    # Highlight selected point by drawing over top with a yellow circle
    if len(points) > 0:
        pygame.draw.circle(window, Data.YELLOW, points[point_index].pos, Data.THICKNESS)


# Main game loop
while running:
    """Continuously checks for user input and mouse events, refreshes, draws to, and updates the window until the
    program is closed
    """
    
    # Gets each event
    for event in pygame.event.get():
        
        # Quits out of the game
        if event.type == pygame.QUIT:
            running = False
        
        # User is dragging a point across the screen if left click is selected and being dragged down
        elif event.type == pygame.MOUSEMOTION and event.buttons[0] and len(points) > 0:
            
            # Get position of mouse
            position = pygame.mouse.get_pos()
            
            # Finds index of point clicked on
            point_index = point_clicked_on(position)

            # Sets new selected point if necessary, and repositions said point to the closest point on the circumference
            if points[point_index].is_draggable:
                points[point_index].pos = circle.closest_point_on_circumference(position)

            # Readjust the points' positions
            adjust_point(point_index, points[point_index].pos)
        
        # If left mouse button is clicked, the user is selecting a button option
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
    
            # Gets position of mouse
            position = pygame.mouse.get_pos()
    
            # If the theorem button is selected, toggle the display of all buttons
            if within(buttons[0].pos, buttons[0].size, position):
                for button in buttons[1:]:
                    button.is_shown = not button.is_shown
    
            # Constructs an inscribed angle
            elif within(buttons[1].pos, buttons[1].size, position):
        
                inscribed_angle()
    
            # Constructs a cyclic quadrilateral
            elif within(buttons[2].pos, buttons[2].size, position):
        
                cyclic_quadrilateral()
    
            # Constructs a triangle with one edge as diameter
            elif within(buttons[3].pos, buttons[3].size, position):
        
                thales()
    
            # Constructs shape which corresponds to the same arc theorem
            elif within(buttons[4].pos, buttons[4].size, position):
        
                same_arc()
    
            # Makes tangent line
            elif within(buttons[5].pos, buttons[5].size, position):
        
                tangent()
    
    # Repaints over the surface with black
    window.fill(Data.BLACK)
    
    # Draws everything to the window
    draw()
    
    # Updates display drawn
    pygame.display.update()
