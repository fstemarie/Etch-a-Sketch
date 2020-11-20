""" Game of Etch-a-Sketch """

import pygame
# pylint: disable=no-name-in-module
from pygame.constants import (
    QUIT, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE)
# pylint: enable=no-name-in-module


RADIUS = 4  # Radius of the circle drawn on the gameboard


def main():
    """Starts Etch-a-Sketch"""

    screen_size = (640, 480)  # Size of the game board
    pos_x = 0
    pos_y = 0

    # initialize the pygame module
    # pylint: disable=no-member
    pygame.init()
    # pylint: enable=no-member

    # load and set the logo
    logo = pygame.image.load("32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Etch-a-Sketch")

    # create a surface on screen
    screen = pygame.display.set_mode(screen_size)
    screen.fill(pygame.Color("grey"))
    pygame.display.flip()

    running = True
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == QUIT:
                # change the value to False, to exit the main loop
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    screen.fill(pygame.Color("grey"))

        # if one or more of the arrow keys are pressed, change the cursor's position
        # Since I am not waiting for a KEYDOWN event, I can press multiple keys at the same time
        if pygame.key.get_pressed()[K_UP]:
            if pos_y > 0:  # Check boundaries
                pos_y -= 1
        if pygame.key.get_pressed()[K_DOWN]:
            if pos_y < screen_size[1] - 1:  # Check boundaries
                pos_y += 1
        if pygame.key.get_pressed()[K_LEFT]:
            if pos_x > 0:  # Check boundaries
                pos_x -= 1
        if pygame.key.get_pressed()[K_RIGHT]:
            if pos_x < screen_size[0] - 1:  # Check boundaries
                pos_x += 1

        # Draw a circle at the cursor's position
        pygame.draw.circle(screen,
                           color=pygame.Color("black"),
                           center=(pos_x, pos_y),
                           radius=RADIUS)
        pygame.display.flip()
        pygame.time.wait(2)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
