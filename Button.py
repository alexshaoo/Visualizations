import pygame
import pygame.freetype

from Data import Data


class Button(pygame.Rect):
    """Docstring about class
    
    
    """
    
    def __init__(self, pos, size, text, fill_colour, border_colour, is_shown, window, font, description):
        
        # Inherit methods and properties of pygame rectangles
        super().__init__(pos, size)
        
        # Position of top left corner of button
        self.pos = pos
        
        # Tuple of width and size of button
        self.size = size
        self.text = text
        self.fill_colour = fill_colour
        self.border_colour = border_colour
        self.is_shown = is_shown
        self.window = window
        self.font = font
        self.description = description
    
    # Draws button onto window
    def draw(self):
        if self.is_shown:
            pygame.draw.rect(self.window, self.border_colour, self, 3)
            pygame.draw.rect(self.window, self.fill_colour, self)
            
            # Shifts text position
            text_pos = (self.pos[0] + 10, self.pos[1] + 10)
            
            self.font.render_to(self.window, text_pos, self.text, self.border_colour)
    
    # Displays the button's description onto a place on the screen
    def show_description(self):
        
        for index, text in enumerate(self.description):
            Data.FONT.render_to(self.window, (0, 520 + 20 * index), text, Data.WHITE)
