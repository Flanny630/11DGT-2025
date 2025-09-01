# My final game submission
# Flanny Xue
# Version 1_4
# August 2025
# TODO: Create a start again button on the finish page. (done)

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
BUSH_IMAGE = pygame.transform.scale(BUSH_IMAGE, (80, 60))  

# Loading the start page image
START_PAGE_IMAGE = pygame.image.load("start_page.png")
START_PAGE_IMAGE = pygame.transform.scale(START_PAGE_IMAGE, (WIDTH, HEIGHT)) # Scale it to start where the screen starts

# Loading the info icon image
INFO_ICON_IMAGE = pygame.image.load("info_icon.png") 
INFO_ICON_IMAGE = pygame.transform.scale(INFO_ICON_IMAGE, (47, 47))  # Make it small for game screen

# Loading the info popup image
INFO_POPUP_IMAGE = pygame.image.load("info_page2.png")
INFO_POPUP_IMAGE = pygame.transform.scale(INFO_POPUP_IMAGE,(WIDTH,HEIGHT)) # Scale it to start where the screen starts

# Loading the finish page image
FINISH_PAGE_IMAGE = pygame.image.load("finish_page.png")
FINISH_PAGE_IMAGE = pygame.transform.scale(FINISH_PAGE_IMAGE, (WIDTH, HEIGHT)) # Scale it to start where the screen starts

# Loading the (back) home button image
HOME_BUTTON_IMAGE = pygame.image.load("home_button.png")
HOME_BUTTON_IMAGE = pygame.transform.scale(HOME_BUTTON_IMAGE, (140, 60))

# Loading the start (again) icon image
START_AGAIN_IMAGE = pygame.image.load("start_again_image.png")
START_AGAIN_IMAGE = pygame.transform.scale(START_AGAIN_IMAGE, (180, 80)) 

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
HORIZON_LINE = 250 

# Setting up the font of all texts
FONT = pygame.font.SysFont("comicsans", 30)

def show_start_page():

    waiting_for_start = True
    show_info_popup = False
    
    # Info icon position (top right corner)
    info_icon_x = WIDTH - 95  # appear 85 pixels away from the right edge
    info_icon_y = 30  # appear 30 pixels from top
    info_icon_rect = pygame.Rect(info_icon_x, info_icon_y, 47, 47)  # Create the rectangle for clicking
    
    while waiting_for_start:
        # Display the starting image
        WIN.blit(START_PAGE_IMAGE, (0, 0))
        
        # Draw the info icon
        WIN.blit(INFO_ICON_IMAGE, (info_icon_x, info_icon_y))
        
        # If the info popup is shown, draw the fullscreen image
        if show_info_popup:
            # Draw the info popup image to fill the whole screen
            WIN.blit(INFO_POPUP_IMAGE, (0, 0))
        
        pygame.display.update()
        
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False  # Exit the program
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Space key pressed
                    if show_info_popup:
                        show_info_popup = False  # Close popup if it's open
                    else:
                        waiting_for_start = False
                        return True  # Start the game if popup is closed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = event.pos
                    # Check if clicked on info icon (only when popup is not shown)
                    if not show_info_popup and info_icon_rect.collidepoint(mouse_x, mouse_y):
                        show_info_popup = True
    
    return True

def draw(player, player_image, elapsed_time, plants, bushes):
    WIN.blit(BG, (0, 0))

    # Rendering the seconds into words which would show as e.g "2s" in white
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    # Drawing the info icon in top right corner (during the game)
    info_icon_x = WIDTH - 75  # 50 pixels from right edge
    info_icon_y = 20  # 10 pixels from top
    WIN.blit(INFO_ICON_IMAGE, (info_icon_x, info_icon_y))

    # Drawing the plant images FIRST (so they appear behind player)
    for plant in plants:
        # Draw image at original position 
        image_x = plant.x - PLANT_WIDTH // 4
        image_y = plant.y - PLANT_HEIGHT // 4
        WIN.blit(PLANT_IMAGE, (image_x, image_y))
    
    # Drawing the bush images SECOND (so they appear behind player)
    for bush in bushes:
        # Draw image at original position (
        image_x = bush.x - BUSH_WIDTH // 4
        image_y = bush.y - BUSH_HEIGHT // 4
        WIN.blit(BUSH_IMAGE, (image_x, image_y))

    # Placing the character LAST (so it appears on top of everything)
    WIN.blit(player_image, (player.x, y))

    pygame.display.update()

def show_finish_page():
    # Adding "restart' and "home" buttons to the finish page

    # Start again button's position - bottom right corner of the finish page
    start_again_x = WIDTH - 210  # 210 pixels away from the right edge
    start_again_y = HEIGHT - 100  # 100 pixels away from the bottom edge
    start_again_rect = pygame.Rect(start_again_x, start_again_y, 180, 80)

    # Home button's position - bottom left corner of the finish page
    home_button_x = 20  # 20 pixels from left edge
    home_button_y = HEIGHT - 85  # 85 pixels away from the bottom edge 
    home_button_rect = pygame.Rect(home_button_x, home_button_y, 140, 60)

    # Show finish page and wait for events
    while True:
        # Display the finish page image fullscreen
        WIN.blit(FINISH_PAGE_IMAGE, (0, 0))

        # Draw the start again button 
        WIN.blit(START_AGAIN_IMAGE, (start_again_x, start_again_y))

        # Draw the home button
        WIN.blit(HOME_BUTTON_IMAGE, (home_button_x, home_button_y))

        pygame.display.update()
        
        # Check for events (still need to handle window closing)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"  # Exit the function
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    # Check if clicked on start again button
                    if start_again_rect.collidepoint(mouse_x, mouse_y):
                        return "restart"  # Signal to restart the game
                    
                    # Check if the player has clicked on the home button
                    elif home_button_rect.collidepoint(mouse_x, mouse_y):
                        return "home"  # Signal to go back to start page

# Main game loop
def main():
    while True:  # Outer loop for game restarts
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
        run = True

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
                    pygame.quit()
                    return "quit"
            
            # Movement code (player)
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

            if hit:
                # Show finish page and get user choice
                choice = show_finish_page()
                if choice == "restart":
                    break  # Break from inner loop to restart the game
                elif choice == "home":
                    return "home"  # Return to start page
                elif choice == "quit":
                    return "quit"  # Exit completely

            # Calling the draw function with both plants and bushes
            draw(player, player_image, elapsed_time, plants, bushes)

if __name__ == "__main__":
    # Game restart loop
    while True:
        # Show starting page first
        if show_start_page():
            result = main()  # Start the game if space was pressed
            if result == "quit":
                break  # Exit if game was quit
            # If result is "home", the loop continues and shows start page again
        else:
            break # Exit if start page was closed
