import math

import pygame

pygame.init()

# Check for if pygame is running in main game loop
running = True

# Dimensions of canvas
WIDTH = 1200
HEIGHT = 800

# Create window to draw on
window = pygame.display.set_mode((WIDTH, HEIGHT))

title = "Cyclic Quadrilaterals"
pygame.display.set_caption(title)

# Radius and center of big circle, as well as thickness of both circle and lines
RADIUS = 300
CIRCLE_THICKNESS = 10
CENTER = (WIDTH // 2, HEIGHT // 2)

# Points on circumference (higher constant multiple smoother movement)
NUMBER_OF_POINTS_ON_CIRCUMFERENCE = 10 * RADIUS

# Colour of lines, circles, and dots
LINE_COL = [255, 0, 0]
CIRCLE_COL = [255, 255, 255]
DOT_COL = [0, 0, 255]

# Cyclic Quadrilaterals always have 4 vertices
points = [[CENTER[0], CENTER[1] - RADIUS], [CENTER[0] + RADIUS, CENTER[1]],
          [CENTER[0], CENTER[1] + RADIUS], [CENTER[0] - RADIUS, CENTER[1]]]

# Index of point that's selected, default to first point
point_index = 0

# Points found on the circumference of the circle
points_on_circumference = []

# Find points on circumference
for i in range(NUMBER_OF_POINTS_ON_CIRCUMFERENCE):
    # X and Y values
    x = RADIUS * math.sin((2 * math.pi / NUMBER_OF_POINTS_ON_CIRCUMFERENCE) * i) + CENTER[0]
    y = RADIUS * math.cos((2 * math.pi / NUMBER_OF_POINTS_ON_CIRCUMFERENCE) * i) + CENTER[1]

    # Add tuple of points to list of points on the circumference
    points_on_circumference.append((int(x), int(y)))


# Calculates distance between two points
def distance_between(point1, point2):
    # Gets x and y distance between points
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]

    # Returns distance via good ol Pythagoras
    return math.sqrt(dx ** 2 + dy ** 2)


# Finds index of point clicked on
def point_clicked_on(possible_points, pos):
    global point_index

    # Checks every point
    for point in possible_points:

        # Returns index of point point clicked on
        if abs(point[0] - pos[0]) <= CIRCLE_THICKNESS and abs(point[1] - pos[1]) <= CIRCLE_THICKNESS:
            return points.index(point)

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
def calculate_angle(start_point, end_point):
    # Horizontal difference between starting and end point
    dx = end_point[0] - start_point[0]

    # Because positive y direction is down
    dy = start_point[1] - end_point[1]

    return math.atan2(dy, dx)


# Draws arc sector angle between two lines
def draw_angle(point1, point2, point3):
    # Radius of arc-circle
    R = 20

    # Rectangle arc will be inscribed in
    rect = pygame.Rect(point2[0] - R, point2[1] - R, 2 * R, 2 * R)

    # Angle of line connecting points 2 and 1 and the x-axis
    angle21 = calculate_angle(point2, point1)

    # Angle of line connecting points 2 and 3 and the x-axis
    angle23 = calculate_angle(point2, point3)

    if angle21 < angle23:
        pygame.draw.arc(window, (255, 0, 255), rect, angle21, angle23, 10)

    elif angle21 > angle23:
        pygame.draw.arc(window, (255, 0, 255), rect, angle23, angle21, 10)


# Main loop
while running:

    for event in pygame.event.get():

        # Quits game
        if event.type == pygame.QUIT:
            running = False

        # If mouse is moving and left click is selected
        elif event.type == pygame.MOUSEMOTION and event.buttons[0]:

            # Get position of mouse
            pos = pygame.mouse.get_pos()

            # Finds index of point clicked on
            point_index = point_clicked_on(points, pos)

            # Sets
            points[point_index] = closest_point(pos)
            point_selected = points[point_index]

    # Draws big circle
    pygame.draw.circle(window, CIRCLE_COL, CENTER, RADIUS, CIRCLE_THICKNESS)

    # Draws lines connecting points
    for j in range(len(points)):
        pygame.draw.line(window, LINE_COL, points[j], points[(j + 1) % len(points)], 1)

    # Draws points on circle
    for point in points:
        pygame.draw.circle(window, CIRCLE_COL, point, CIRCLE_THICKNESS)

    # Draws angle between selected point and adjacent points
    draw_angle(points[(point_index - 1) % len(points)], points[point_index], points[(point_index + 1) % len(points)])
    draw_angle(points[(point_index + 1) % len(points)], points[(point_index + 2) % len(points)],
               points[(point_index + 3) % len(points)])

    # Highlight selected point by drawing over top with a yellow circle
    pygame.draw.circle(window, [255, 255, 0], points[point_index], CIRCLE_THICKNESS)

    # Updates display drawn
    pygame.display.update()

    # Repaints over the surface with
    window.fill((0, 0, 0))
