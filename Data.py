import pygame
import pygame.freetype as freetype

# Initialize freetype module
pygame.init()


class Data:
    """This class is responsible for keeping track of all the data
    
    Attributes
    ----------
    :cvar WIDTH: int
        Width of surface
    :cvar HEIGHT: int
        Height of surface
    :cvar CENTER: tuple
        Location (x and y) of the center of the surface
    :cvar TITLE: string
        Title of the pygame
    :cvar FONT: pygame.font
        Font of text
    :cvar THICKNESS: int
        Both the thickness of the circle and the
    :cvar NUMBER_OF_POINTS: int
        The number of points that will be found on the circle
    :cvar ARC_RADIUS: int
        The radius of the arcsector drawn to indicate an angle measure
    :cvar theorem_names: list
        Contains the names of each theorem, in order, which the buttons will be displaying
    :cvar descriptions: list
        A list containing descriptions for each theorem, in order. Will be displayed when button is selected
    """
    
    # Colour constants
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    DARK_GREEN = (0, 100, 0)
    BLUE = (0, 0, 255)
    PURPLE = (255, 0, 255)
    
    WIDTH = 1000
    HEIGHT = 600
    
    CENTER = (WIDTH // 2, HEIGHT // 2)
    
    TITLE = "Geometry Visualizations"
    
    FONT = freetype.SysFont(pygame.font.get_default_font(), 16)
    
    THICKNESS = 8
    
    NUMBER_OF_POINTS = 4
    
    ARC_RADIUS = 25
    
    theorem_names = ["Angle at Center", "Cyclic Quadrilateral", "Thales' Theorem", "Subtended by Same Arc",
                     "Tangent Line"]
    
    descriptions = [["An inscribed angle is an angle formed by three points on the circumference of a circle.",
                     "A central angle is an angle formed by two points on the circumference of a circle, and the center of that circle.",
                     "on the circumference will always be half of the central angle."],
                    ["A cyclic quadrilateral is a 4 sided shape which have all of its vertices.",
                     "Opposite angles on a cyclic quadrilateral will always add up to 180 degrees."],
                    ["This applies to triangles which have two vertices on diametrically opposite sides of a circle.",
                     "It states that the angle formed between those two vertices and another will always be a right angle."],
                    ["Angles that are on the same arc with the same endpoints as each other will be equal.",
                     "This theorem is also known as the 'Angles Subtended by the Same Arc Theorem'.",
                     "(But that was too long so I changed it to this instead)"],
                    ["A line is drawn tangent to a point on a circle's circumference.",
                     "This line will always form a right angle with the line connecting the circle's center with its point of tangency."]]
