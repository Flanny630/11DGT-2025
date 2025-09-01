# My final game submission
# Flanny Xue
# Version 1_4
# August 2025
# TODO: Set the projecitles to start at the new horizon line (done)

# Import the pygame library to use it
import pygame
import time
import random
from pygame import image as img
pygame.font.init()

# Setting the size of the display window (constant values)
WIDTH, HEIGHT = 600, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Setting the caption/title for the game
pygame.display.set_caption("Tane and the Three Baskets of Knowledge") 

# Importing my background image
BG = pygame.image.load("bg2.jpeg")
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

# Loading and scaling the plant image
PLANT_IMAGE = pygame.image.load("plant.png")
PLANT_IMAGE = pygame.transform.scale(PLANT_IMAGE, (64, 65))

# Loading and scaling the bush image
BUSH_IMAGE = pygame.image.load("bush.png")
BUSH_IMAGE = pygame.transform.scale(BUSH_IMAGE, (80, 60))  # Making bush a bit wider

# Width and height of sprite
Player_width = 107
Player_height = 186

# Co-ordinates for player to start
x = 250
y = 520

# Set the velocity to control speed of sprite and obstacles
Player_vel = 5 
Plant_vel = 5
Bush_vel = 2  # Bush moves slower than plants

# Set the plant's width and height
PLANT_WIDTH = 40
PLANT_HEIGHT = 60

# Set the bush's width and height
BUSH_WIDTH = 80
BUSH_HEIGHT = 60

# Set the horizon line where projectiles start appearing 
HORIZON_LINE = 260  

# Setting up the font of all texts
FONT = pygame.font.SysFont("comicsans", 30)

# Inserting the image as background
def draw(player, player_image, elapsed_time, plants, bushes):
    WIN.blit(BG, (0, 0))

    # Rendering the seconds into words which would show as e.g "2s" in white
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    # Drawing the plant images FIRST (so they appear behind player)
    for plant in plants:
        # Draw image at original position 
        image_x = plant.x - PLANT_WIDTH // 4
        image_y = plant.y - PLANT_HEIGHT // 4
        WIN.blit(PLANT_IMAGE, (image_x, image_y))
    
    # Drawing the bush images SECOND (so they appear behind player)
    for bush in bushes:
        # Draw image at original position 
        image_x = bush.x - BUSH_WIDTH // 4
        image_y = bush.y - BUSH_HEIGHT // 4
        WIN.blit(BUSH_IMAGE, (image_x, image_y))

    # Placing the character LAST (so it appears on top of everything)
    WIN.blit(player_image, (player.x, y))

    pygame.display.update()

# Main game loop
def main():
    run = True

    # Loading player_image and adding the rect around to player to detect collisions
    player_image = img.load("G_back.png")
    player_image = pygame.transform.scale(player_image, (122, 212))
    
    # Making collision rectangle smaller - only covers lower body
    collision_height = Player_height // 2  # Half the height (lower body only)
    collision_y_offset = Player_height - collision_height  # Start from middle of player
    player = pygame.Rect(x, y + collision_y_offset, Player_width, collision_height)

    # Creating a clock object to make sure it moves at a constant speed
    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0

    # Adding plant projectiles (obstacles)
    plant_add_increment = 2000
    plant_count = 0

    # Adding bush projectiles (obstacles)
    bush_add_increment = 4000  # Bush appears less frequently
    bush_count = 0

    plants = []
    bushes = []
    hit = False

    while run: 
        plant_count += clock.tick(60)
        bush_count += clock.tick(60)  # Same tick for bush timing
        elapsed_time = time.time() - start_time

        # Creating the plants (start from horizon line)
        if plant_count > plant_add_increment: 
            for _ in range(3):
                plant_x = random.randint(0, WIDTH - PLANT_WIDTH)
                # Making smaller collision rectangle for plant (centered)
                smaller_plant_width = PLANT_WIDTH // 2  # Half the width
                smaller_plant_height = PLANT_HEIGHT // 2  # Half the height
                offset_x = PLANT_WIDTH // 4  # Center the smaller rectangle
                offset_y = PLANT_HEIGHT // 4  # Center the smaller rectangle
                plant = pygame.Rect(plant_x + offset_x, HORIZON_LINE + offset_y, smaller_plant_width, smaller_plant_height)
                plants.append(plant) 

            plant_add_increment = max(200, plant_add_increment - 50)
            plant_count = 0

        # Creating the bushes (only 1 at a time, start from horizon line)
        if bush_count > bush_add_increment:
            bush_x = random.randint(0, WIDTH - BUSH_WIDTH)
            # Making smaller collision rectangle for bush (centered)
            smaller_bush_width = BUSH_WIDTH // 2  # Half the width
            smaller_bush_height = BUSH_HEIGHT // 2  # Half the height
            offset_x = BUSH_WIDTH // 4  # Center the smaller rectangle
            offset_y = BUSH_HEIGHT // 4  # Center the smaller rectangle
            bush = pygame.Rect(bush_x + offset_x, HORIZON_LINE + offset_y, smaller_bush_width, smaller_bush_height)
            bushes.append(bush)
            
            bush_add_increment = max(3000, bush_add_increment - 100)  # Minimum 3 seconds between bushes
            bush_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break 
        
        # Movement code
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - Player_vel >= 0:
            player.x -= Player_vel
        if keys[pygame.K_RIGHT] and player.x + Player_vel + Player_width <= WIDTH:
            player.x += Player_vel

        # Move the plants
        for plant in plants[:]:
            plant.y += Plant_vel 
            if plant.y > HEIGHT:
                plants.remove(plant)
            elif plant.y + plant.height >= player.y and plant.colliderect(player):
                plants.remove(plant)
                hit = True
                break

        # Move the bushes (slower)
        for bush in bushes[:]:
            bush.y += Bush_vel  # Bushes move slower
            if bush.y > HEIGHT:
                bushes.remove(bush)
            elif bush.y + bush.height >= player.y and bush.colliderect(player):
                bushes.remove(bush)
                hit = True
                break

        # Drawing the finishing page / got hit page onto the window
        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
        
        # Calling the draw function with both plants and bushes
        draw(player, player_image, elapsed_time, plants, bushes)
    
    pygame.quit()

if __name__ == "__main__":
    main()
