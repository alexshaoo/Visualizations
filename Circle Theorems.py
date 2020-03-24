import math

import pygame
import pygame.freetype

from Point import Point

pygame.init()

# Check for if pygame is running in main game loop
running = True

# Dimensions of canvas
WIDTH = 1200
HEIGHT = 600

# Create window to draw on
window = pygame.display.set_mode((WIDTH, HEIGHT))

title = "Cyclic Quadrilaterals"
pygame.display.set_caption(title)

# Radius and center of big circle, as well as thickness of both circle and lines
RADIUS = 200
CIRCLE_THICKNESS = 8
CENTER = (WIDTH // 2, HEIGHT // 2)

# Points on circumference (higher constant multiple smoother movement)
NUMBER_OF_POINTS_ON_CIRCUMFERENCE = int(2 * math.pi * RADIUS)

# Lines are red
LINE_COL = [255, 0, 0]

# Big Circle is white
CIRCLE_COL = [255, 255, 255]

# Dots/Points are blue
DOT_COL = [0, 0, 255]

# For theorems that involve 4 points
pointA = Point("A", CIRCLE_THICKNESS, [CENTER[0] + RADIUS, CENTER[1]], DOT_COL, 0)
pointB = Point("B", CIRCLE_THICKNESS, [CENTER[0], CENTER[1] - RADIUS], DOT_COL, 90)
pointC = Point("C", CIRCLE_THICKNESS, [CENTER[0] - RADIUS, CENTER[1]], DOT_COL, 180)
pointD = Point("D", CIRCLE_THICKNESS, [CENTER[0], CENTER[1] + RADIUS], DOT_COL, 270)
points = [pointA, pointB, pointC, pointD]

# Index of point that's selected, default to 1st point
point_index = 0

# Points found on the circumference of the circle
# Selected point position defaults to these
points_on_circumference = []

# 'Radius' of arcsector used for drawing angle
ARC_RADIUS = 25

FONT = pygame.freetype.SysFont('Ubuntu', 16)


# Calculate approximate points on circumference
def find_points_on_circumference(number_of_points):
    global points_on_circumference

    # Resets the list of points on the circumference
    points_on_circumference = []

    for j in range(number_of_points):
        # X and Y values of the points
        x = RADIUS * math.sin((2 * math.pi / number_of_points) * j) + CENTER[0]
        y = RADIUS * math.cos((2 * math.pi / number_of_points) * j) + CENTER[1]

        # Round points to nearest int and add as a tuple of new points on the circumference
        points_on_circumference.append((int(x), int(y)))


# Given their position, calculates distance between two points
def distance_between(pos1, pos2):
    # Gets x and y distance between points
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]

    # Returns distance via good ol Pythagoras
    return math.sqrt(dx ** 2 + dy ** 2)


# Finds point clicked on
def point_clicked_on(pos):
    global points

    # Checks every point
    for dot in points:

        # Returns index of point clicked on
        if abs(dot.pos[0] - pos[0]) <= CIRCLE_THICKNESS and abs(dot.pos[1] - pos[1]) <= CIRCLE_THICKNESS:
            return points.index(dot)

    # If all points are searched and none are found, return index of original point that was selected
    return point_index


# Finds point on circumference closest to a position
# Used to locate point closest to mouse drag
def closest_point(pos):
    # Default closest point to first point on circumference
    closest = points_on_circumference[0]
    shortest_distance = distance_between(CENTER, closest)

    # Checks each dot on the circumference
    for dot in points_on_circumference:

        # Find distance between point and the position
        distance = distance_between(pos, dot)

        # Sets new closest point and distance if a closer point is found
        if distance < shortest_distance:
            closest = dot
            shortest_distance = distance

    # Returns closest point on circumference
    return closest


# Calculates angle between a line and the positive x axis
def calculate_angle(start_pos, end_pos):
    # Horizontal difference between starting and end point
    dx = end_pos[0] - start_pos[0]

    # Flipped because positive y direction is down
    dy = start_pos[1] - end_pos[1]

    angle = math.atan2(dy, dx)

    # Return angle between 0 and 2*pi
    if angle < 0:
        return 2 * math.pi + angle
    else:
        return angle


# Draws arc sector angle between two lines, BA and BC
def draw_angle(A, B, C, colour):
    # Rectangle arc will be inscribed in
    rect = pygame.Rect(B.pos[0] - ARC_RADIUS, B.pos[1] - ARC_RADIUS, 2 * ARC_RADIUS, 2 * ARC_RADIUS)

    # Angle of line connecting points A, B, and C to center
    angleA = calculate_angle(A.pos, CENTER)
    angleB = calculate_angle(B.pos, CENTER)
    angleC = calculate_angle(C.pos, CENTER)

    # Angle of lines AB and BC
    angleABO = calculate_angle(B.pos, A.pos)
    angleBCO = calculate_angle(B.pos, C.pos)

    # Checking and drawing angle
    if angleC < angleB < angleA or angleB < angleA < angleC or angleA < angleC < angleB:
        pygame.draw.arc(window, colour, rect, angleABO, angleBCO)

    elif angleC > angleB > angleA or angleB > angleA > angleC or angleA > angleC > angleB:
        pygame.draw.arc(window, colour, rect, angleBCO, angleABO)


# Calculate the number of points on the circumference first
find_points_on_circumference(NUMBER_OF_POINTS_ON_CIRCUMFERENCE)

# Main loop
while running:

    for event in pygame.event.get():

        # Quits game
        if event.type == pygame.QUIT:
            running = False

        # If mouse is moving and left click is selected
        elif event.type == pygame.MOUSEMOTION and event.buttons[0]:

            # Get position of mouse
            position = pygame.mouse.get_pos()

            # Finds index of point clicked on
            point_index = point_clicked_on(position)

            # Sets new selected point, and position of that point to the new position on the circumference
            points[point_index].pos = closest_point(position)
            point_selected = points[point_index]

    # Repaints over the surface with
    window.fill((0, 0, 0))

    # Draws big circle
    pygame.draw.circle(window, CIRCLE_COL, CENTER, RADIUS, CIRCLE_THICKNESS)

    # Draws points and lines connecting points
    for starting_point, ending_point in zip(points[:-1], points[1:]):
        starting_point.draw_line(ending_point, window, LINE_COL)

    # Connects first and last point to form closed loop
    points[-1].draw_line(points[0], window, LINE_COL)

    for point in points:
        point.draw(window)

        # Calculates angle between each point and center of circle
        point.calculate_angle(CENTER)

        # Gets the angle of the point in degrees
        angle_in_degrees = int(180 * point.angle / math.pi)

        # Calculates place to display angle, readjust to give top right position of text placement

        display_angle_position = (point.pos[0] - 40 * math.cos(point.angle) - 9,
                                  point.pos[1] + 40 * math.sin(point.angle) - 5)

        # Convert from radians to degrees for display
        FONT.render_to(window, display_angle_position, str(angle_in_degrees), (255, 255, 255))

    # Highlight selected point by drawing over top with a yellow circle
    pygame.draw.circle(window, [255, 255, 0], points[point_index].pos, CIRCLE_THICKNESS)

    # Draws angle between selected point and adjacent points
    for i in range(len(points)):
        points_to_form_angle_with = (points[(point_index + i) % len(points)],
                                     points[(point_index + i + 1) % len(points)],
                                     points[(point_index + i + 2) % len(points)])

        # Unpacks tuple arguments and send in as arguments
        if i % 2 == 0:
            draw_angle(*points_to_form_angle_with, (255, 0, 255))

        else:
            draw_angle(*points_to_form_angle_with, (0, 255, 255))

    # Updates display drawn
    pygame.display.update()
