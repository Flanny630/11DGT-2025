# My final game submission
# Flanny Xue
# Version 1_1
# June 2025
# TODO: to create a main window (done)

# Import the pygame library to use it
import pygame
import time
import random

# # Setting the size of the display window (constant values)
WIDTH, HEIGHT = 700, 800
WIN = pygame. display.set_mode((WIDTH, HEIGHT))

# Setting the caption/title for the game
pygame. display.set_caption("Tane and the Three Baskets of Knowledge") 

# Main game loop
def main():
    run = True

    while run: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break 
    
    pygame.quit()

if __name__ == "__main__":
    main()
