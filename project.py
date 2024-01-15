# Programmer : Alexander Walker
# Description: 

# Import and initialize the pygame library
import pygame
import random
from math import atan, degrees
from pygame.locals import *
pygame.init()

# Import functions for drawing gridlines and using sprites
from pygame_grid import make_grid
from ucc_sprite import Sprite

### SET UP GLOBAL CONSTANTS HERE
WIDTH = 640
HEIGHT = 640
BACKGROUND_COLOR = "black"
TIME = 900


#-=-=-=-=-(Bullet configure)-=-=-=-=-
#Controls the starting speed of the bullet
bullet_speed = 4

#Control the spawn location of the bullet
x_r = 0
y_r = random.randint(100, 200)

time1 = 900
time2 = 60

#-=-=-=-=-(Player configure)-=-=-=-=-
#Controls the starting speed of the player
plr_speed = 2

plr_x = WIDTH / 2
plr_y = 400

# Create and open a pygame screen with the given size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
grid = make_grid()


# Set the title of the pygame screen
pygame.display.set_caption("My Game")

# Create a clock to keep track of time
clock = pygame.time.Clock()

# Group to hold all of the active sprites
all_sprites = pygame.sprite.LayeredUpdates()
bullets = pygame.sprite.LayeredUpdates()

### SET UP YOUR GAME HERE

#-=-=-=-=-=-(Load Images)-=-=-=-=-=-=-

#Player Images.
player1_image = pygame.image.load("Player1.png")
player1_image = pygame.transform.rotozoom(player1_image, 0, 0.80)
player2_image = pygame.image.load("Player2.png")
player2_image = pygame.transform.rotozoom(player2_image, 0, 0.80)

#Bullet Images
bullet1_image = pygame.image.load("Bullet1.png")
bullet1_image = pygame.transform.rotozoom(bullet1_image, 90, 0.9)

#Hp Bar Images
Bar1_image = pygame.image.load("Bar1.png")
Bar1_image = pygame.transform.rotozoom(Bar1_image, 0, 0.8)
Bar2_image = pygame.image.load("Bar2.png")
Bar2_image = pygame.transform.rotozoom(Bar2_image, 0, 0.8)
Bar3_image = pygame.image.load("Bar3.png")
Bar3_image = pygame.transform.rotozoom(Bar3_image, 0, 0.8)
Bar4_image = pygame.image.load("Bar4.png")
Bar4_image = pygame.transform.rotozoom(Bar4_image, 0, 0.8)
Bar5_image = pygame.image.load("Bar5.png")
Bar5_image = pygame.transform.rotozoom(Bar5_image, 0, 0.8)
Bar6_image = pygame.image.load("Bar6.png")
Bar6_image = pygame.transform.rotozoom(Bar6_image, 0, 0.8)

#Warning Image
Warning_image = pygame.image.load("Warning.png")
Warning_image = pygame.transform.rotozoom(Warning_image, 0, 1)
#-=-=-=-=-=-(Create Sprites)-=-=-=-=-=-

#Player Sprite.
player = Sprite(player1_image)
player.center = (plr_x, plr_y)
player.add(all_sprites)
player.image_num = 1
player.count = 0

#HP Sprite
HP_bar = Sprite(Bar1_image)
HP_bar.center = (WIDTH / 2, 595)
HP_bar.add(all_sprites)
HP_bar.hp_num = 1

#Create a timer for the countdown clock
SPAWNCLOCK = pygame.event.custom_type()
pygame.time.set_timer(SPAWNCLOCK, time1)

#WARNING = pygame.event.custon_type()
#pygame.time.set_timer(WARNING, time2)

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
            
            
        #-=-=-=-(Warning Attack)-=-=-=-
        #if event.type == WARNING:
            
        
        
        #-=-=-=-(Tracking Bullet)-=-=-=-
        if event.type == SPAWNCLOCK:
            
            y_r = random.randint(250, 500)
            bullet_speed += 0.01
            plr_speed += 0.02
            bullet = Sprite(bullet1_image)
            bullet.center = (0, y_r)
            bullet.direction = degrees(atan((y_r - player.centery) / (player.centerx - x_r)))
            bullet.add(all_sprites, bullets)
            bullet.speed = (bullet_speed)
            bullet.count = 0
            bullet.image_num = 1

    ### MANAGE GAME STATE FRAME-BY-FRAME
    
    #-=-=-=-=-(HP BAR)-=-=-=-=-
    for bullet in bullets:
    #If the bullet goes off the screen, wrap around to the other side of the screen
        if bullet.left > WIDTH:
            bullet.kill()
        if bullet.right < 0:
            bullet.kill()
        if bullet.top < 255:
            bullet.kill()
        if bullet.bottom > 550:
            bullet.kill()
            
        if pygame.sprite.collide_mask(player, bullet):
            HP_bar.hp_num += 1
            bullet.kill()
    
        if HP_bar.hp_num == 1:
            HP_bar.image = Bar1_image
            
        elif HP_bar.hp_num == 2:
            HP_bar.kill()
            HP_bar.image = Bar2_image
            HP_bar.add(all_sprites)
            
        elif HP_bar.hp_num == 3:
            HP_bar.kill()
            HP_bar.image = Bar3_image
            HP_bar.add(all_sprites)
        
        elif HP_bar.hp_num == 4:
            HP_bar.kill()
            HP_bar.image = Bar4_image
            HP_bar.add(all_sprites)
        
        elif HP_bar.hp_num == 5:
            HP_bar.kill()
            HP_bar.image = Bar5_image
            HP_bar.add(all_sprites)
    
        elif HP_bar.hp_num == 6:
            HP_bar.kill()
            HP_bar.image = Bar6_image
            HP_bar.add(all_sprites)
            
    #-=-=-=-=-=-(Player Movement)-=-=-=-=-=-
    
    #If the player is alive then.
    if player.alive():
        keys = pygame.key.get_pressed()
        #Moves up if the up arrow is pressed.
        if keys[K_UP] and player.top > 225:
            #Moves up by plr_speed, which can be configured at the top.
            player.y -= plr_speed       
        if keys[K_DOWN] and player.bottom < 550:
            player.y += plr_speed   
        if keys[K_LEFT] and player.left > 0: 
            player.x -= plr_speed
        if keys[K_RIGHT] and player.right < WIDTH:
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
    pygame.draw.rect(screen, (255, 255, 255), (0, 220, WIDTH, 5), 0)
    pygame.draw.rect(screen, (255, 255, 255), (0, 550, WIDTH, 5), 0)

    # Redraw the sprites
    all_sprites.draw(screen)

    # Uncomment the next line to show a grid
    # screen.blit(grid, (0,0))

    # Flip the changes to the screen to the computer display
    pygame.display.flip()
    
# Quit the pygame program
pygame.quit()
