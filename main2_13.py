# My final game submission
# Flanny Xue
# Version 1_2
# June 2025
# TODO: Adding the adjusted sized player image into the game & adding a new placement (done)

# Import the pygame library to use it
import pygame
import time
import random
from pygame import image as img
pygame.font.init()

# # Setting the size of the display window (constant values)
WIDTH, HEIGHT = 600, 750
WIN = pygame. display.set_mode((WIDTH, HEIGHT))

# Setting the caption/title for the game
pygame. display.set_caption("Tane and the Three Baskets of Knowledge") 

# Importing my background image
BG = pygame.image.load("bg.jpeg")
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

# Width and height of sprite
Player_width = 107
Player_height = 186

# Co-ordinates for player to start
x = 250
y = 500

# Set the velocity to control speed of sprite and obstacle
Player_vel = 5 
Plant_vel = 5

# Set the plant's width and height
PLANT_WIDTH = 20
PLANT_HEIGHT= 40

# Setting up the font of all texts
FONT = pygame.font.SysFont("comicsans", 30)

# Inserting the image as background
def draw(player, player_image, elapsed_time, plants): # adding player image parameter
    WIN.blit(BG, (0, 0))

    # Rendering the seconds into words which would show as e.g "2s" in white
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10,10)) # Padding on the screen

    # Placing the character
    WIN.blit(player_image,(player.x, player.y)) # adding player image with player.x and player .y

    # Making the plants
    for plant in plants:
        pygame.draw.rect(WIN, "green", plant)

    pygame.display.update()

# Main game loop
def main():
    run = True

    # Loading player_image and adding the rect around to player to 
    # player image to detect collisions
    player_image = img.load("G_back.png")
    player_image = pygame.transform.scale(player_image, (122, 212))
    player = pygame.Rect(x, y, Player_width, Player_height)

    # Creating a clock object to make sure it moves at a constant speed
    clock = pygame.time.Clock()

    star_time = time.time()
    elapsed_time = 0

    # Adding projectile (obstacles)
    plant_add_increment = 2000 # The first plant will be added in 2000 miliseconds when we start the game
    plant_count = 0

    plants = []
    hit = False

    while run: 
        plant_count += clock.tick(60) # Returning number of millisecond since last tick to keep track of the precise time
        elapsed_time = time.time() - star_time # Gives the number of seconds that have elapsed since we started the game

        # Creating the stars
        # Adding in more plant obstacles as the time increases
        if plant_count > plant_add_increment: 
            for _ in range(3): # Adding 3 stars each time
                plant_x = random.randint(0, WIDTH - PLANT_WIDTH) # Placing the plant in a random position
                plant = pygame.Rect(plant_x, -PLANT_HEIGHT, PLANT_WIDTH, PLANT_HEIGHT) # Make the plant to move down from the top of the screen
                plants.append(plant) 

            plant_add_increment = max(200, plant_add_increment - 50) # Minimum plant add increment ever have is 200
            plant_count = 0 # But since plant at increment is going to be much larger than 200 in the starting case to 2000, it's going to subtract 50 ms

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

        # Move the plant
        # Check if the plant has collided with the player. If they've collided then I want to remove this star because it hit the player. 
        for plant in plants[:]:
            plant.y += Plant_vel 
            if plant.y > HEIGHT:
                plants.remove(plant)
            elif plant.y + plant.height >= player.y and plant.colliderect(player): # '.colliderect' tells us if two rectangles have collided.
                plants.remove(plant)
                hit = True
                break

        # Drawing the finishing page / got hit page onto the window.
        if hit:
            lost_text = FONT.render("You Lost!", 1, "white") # Generate text
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2)) # Draw it onto the screen - positioning the text
            pygame.display.update()
            pygame.time.delay(4000) # Delaying the results in 4 seconds
            break
        
        # Calling the draw function to draw, player rect, player image, elapsed time and the plants
        draw(player, player_image, elapsed_time, plants)
    
    pygame.quit()

if __name__ == "__main__":
    main()
