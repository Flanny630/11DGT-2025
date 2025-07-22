# My final game submission
# Flanny Xue
# Version 1_2
# June 2025
# TODO: Keeping track of time & rendering text (done)

# Import the pygame library to use it
import pygame
import time
import random
pygame.font.init()

# # Setting the size of the display window (constant values)
WIDTH, HEIGHT = 800, 924
WIN = pygame. display.set_mode((WIDTH, HEIGHT))

# Setting the caption/title for the game
pygame. display.set_caption("Tane and the Three Baskets of Knowledge") 

# Importing my background image
BG = pygame.image.load("bg.jpeg")

# Width and height of sprite
Player_width = 80
Player_height = 120

# Set the velocity to control speed of sprite
Player_vel = 5 

# Setting up the font of all texts
FONT = pygame.font.SysFont("comicsans", 30)

# Inserting the image as background
def draw(player, elapsed_time):
    WIN.blit(BG, (0, 0))

    # Rendering the seconds into words which would show as e.g "2s" in white
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10,10)) # Padding on the screen

    # Making the character
    pygame.draw.rect(WIN, "red", player) 

    pygame.display.update()

# Main game loop
def main():
    run = True

    # Placing the player
    player = pygame.Rect(400, HEIGHT - Player_height, Player_width, Player_height)

    # Creating a clock object to make sure it moves at a constant speed
    clock = pygame.time.Clock()

    star_time = time.time()
    elapsed_time = 0

    while run: 
        clock.tick(60)
        elapsed_time = time.time() - star_time #gives the number of seconds that have elapsed since we started the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break 
        
        # Movement code
        # Moves character for as long as the key gets held down in whatever direction I choose
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - Player_vel >= 0:
            player.x -= Player_vel
        if keys[pygame.K_RIGHT] and player.x + Player_vel + Player_width <= WIDTH:
            player.x += Player_vel



        draw(player, elapsed_time)
    
    pygame.quit()

if __name__ == "__main__":
    main()
