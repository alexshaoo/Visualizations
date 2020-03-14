# import a library of functions called 'pygame'
import pygame

# intialize the game engine
pygame.init()
pygame.font.init()

# defining colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 128, 0)

pi = 3.141592653

# Set the width and height of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)

# setting the window title
pygame.display.set_caption("Aww yea")

# Loop until the user clicks the close button.
done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.arc(screen, green, [162, 162, 224, 75], pi / 2, pi, 2)
    pygame.draw.arc(screen, black, [164, 164, 224, 75], 0, pi / 2, 2)
    pygame.draw.arc(screen, white, [164, 164, 224, 75], 3 * pi / 2, 2 * pi, 2)
    pygame.draw.arc(screen, blue, [164, 164, 224, 75], pi, 3 * pi / 2, 2)

pygame.quit()
