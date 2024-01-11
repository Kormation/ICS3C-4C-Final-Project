# Programmer : Alexander Walker
# Description: 

# Import and initialize the pygame library
import pygame
from pygame.locals import *
pygame.init()

# Import functions for drawing gridlines and using sprites
from pygame_grid import make_grid
from ucc_sprite import Sprite

### SET UP GLOBAL CONSTANTS HERE
WIDTH = 640
HEIGHT = 640
BACKGROUND_COLOR = "black"


#-=-=-=-=-(Player configure)-=-=-=-=-
#Controls the starting speed of the player
plr_speed = 2

plr_x = 100
plr_y = 100

# Create and open a pygame screen with the given size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
grid = make_grid()
grid.show

# Set the title of the pygame screen
pygame.display.set_caption("My Game")

# Create a clock to keep track of time
clock = pygame.time.Clock()

# Group to hold all of the active sprites
all_sprites = pygame.sprite.LayeredUpdates()

### SET UP YOUR GAME HERE

#-=-=-=-=-=-(Load Images)-=-=-=-=-=-=-

#Player Images.
player1_image = pygame.image.load("Player1.png")
player1_image = pygame.transform.rotozoom(player1_image, 0, 0.80)
player2_image = pygame.image.load("Player2.png")
player2_image = pygame.transform.rotozoom(player2_image, 0, 0.80)

#-=-=-=-=-=-(Create Sprites)-=-=-=-=-=-

#Player Sprite.
player = Sprite(player1_image)
player.center = (plr_x, plr_y)
player.add(all_sprites)
player.image_num = 1
player.count = 0





### DEFINE HELPER FUNCTIONS



# Main Loop
running = True
while running:
    # Set the frame rate to 60 frames per second
    clock.tick(60)

    for event in pygame.event.get():
        # Check if the quit (X) button was clicked
        if event.type == QUIT:
            running = False

        ### MANAGE OTHER EVENTS SINCE THE LAST FRAME
        


    ### MANAGE GAME STATE FRAME-BY-FRAME
    
    
    #-=-=-=-=-=-(Player Movement)-=-=-=-=-=-
    
    #If the player is alive then.
    if player.alive():
        keys = pygame.key.get_pressed()
        #Moves up if the up arrow is pressed.
        if keys[K_UP]:
            #Moves up by plr_speed, which can be configured at the top.
            player.y -= plr_speed       
        if keys[K_DOWN]:
            player.y += plr_speed   
        if keys[K_LEFT]: 
            player.x -= plr_speed
        if keys[K_RIGHT]:
            player.x += plr_speed
        
        #Controls which player sprite is being shown on the screen.
        if keys[K_DOWN] or keys[K_UP] or keys[K_LEFT] or keys[K_RIGHT]:
            player.count += 1
            #Controls how fast the images change.
            if player.count >= 20:
                player.count = 0
                #If player num is == 1 then player2_image will show.
                if player.image_num == 1:
                    player.image = player2_image
                    player.image_num = 2
                #Else the player1_image will be shown.
                else:
                    player.image = player1_image
                    player.image_num = 1

    # Update the sprites' locations
    all_sprites.update()

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)
    
    #-=-=-=-=-=-=-(Screen Design)-=-=-=-=-=-=-
    pygame.draw.rect(screen, (255, 255, 255), (200, 50, 10, 330), 0)

    # Redraw the sprites
    all_sprites.draw(screen)

    # Uncomment the next line to show a grid
    # screen.blit(grid, (0,0))

    # Flip the changes to the screen to the computer display
    pygame.display.flip()
    
# Quit the pygame program
pygame.quit()
