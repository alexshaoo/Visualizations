import pygame
import pygame.freetype

from Data import Data


class Button(pygame.Rect):
    """A button class that takes care of all buttons being drawn to the window and their functionality. Essentially
    just a clickable pygame.Rect object
    """
    
    def __init__(self, pos, size, text, fill_colour, border_colour, is_shown, window, font, description):
        """Initializes a new button object with the given parameters
        
        :param pos: The coordinates (x and y) of the top left corner of the button
        :param size: The dimensions (x and y) of the button's suze
        :param text: The text that will be shown on the button
        :param fill_colour: The colour that fills in the button
        :param border_colour: The colour of the button's border
        :param is_shown: If a button is displayed to the screen
        :param window: The window to which the button will be drawn to
        :param font: The font of the text stored within the button
        :param description: The description of the specific theorem that the button keeps track of
        """
        
        # Inherit methods and properties of pygame rectangles
        super().__init__(pos, size)
        self.pos = pos
        self.size = size
        self.text = text
        self.fill_colour = fill_colour
        self.border_colour = border_colour
        self.is_shown = is_shown
        self.window = window
        self.font = font
        self.description = description
    
    def draw(self):
        """Draws the button to the window
        
        :return:
        """
        if self.is_shown:
            pygame.draw.rect(self.window, self.border_colour, self, 3)
            pygame.draw.rect(self.window, self.fill_colour, self)
            
            # Shifts text position
            text_pos = (self.pos[0] + 10, self.pos[1] + 10)
            
            # Redner the text shown on the button to its designated location
            self.font.render_to(self.window, text_pos, self.text, self.border_colour)
    
    # Displays the button's description onto a place on the screen
    def show_description(self):
        """Displays the button's description to a position on screen
        
        :return:
        """
        
        for index, text in enumerate(self.description):
            # Redner the description of the text to a certain location on screen
            Data.FONT.render_to(self.window, (0, 520 + 20 * index), text, Data.WHITE)
