# My final game submission
# Flanny Xue
# Version 1_2
# June 2025
# TODO: Adding a background image (done)

# Import the pygame library to use it
import pygame
import time
import random

# # Setting the size of the display window (constant values)
WIDTH, HEIGHT = 800, 924
WIN = pygame. display.set_mode((WIDTH, HEIGHT))

# Setting the caption/title for the game
pygame. display.set_caption("Tane and the Three Baskets of Knowledge") 

# Importing my background image
BG = pygame.image.load("bg.jpeg")

# Inserting the image as background
def draw():
    WIN.blit(BG,(0, 0))
    pygame.display.update()

# Main game loop
def main():
    run = True

    while run: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break 
        
        draw()
    
    pygame.quit()

if __name__ == "__main__":
    main()
