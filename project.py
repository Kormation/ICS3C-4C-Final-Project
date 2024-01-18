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
GAME_OVER_COLOR = "white"
BACKGROUND_COLOR = "black"
START_TIME = 75
FONT_COLOR = "white"

#-=-=-=-=-(Bullet configure)-=-=-=-=-
#Controls the starting speed of the bullet
bullet_speed = 4

#Controls the speed of the warning bullet
warning_bullet_speed = 5

#Control the spawn location of the bullet
x_r = 0
y_r = random.randint(100, 200)

time1 = 500
time2 = 800

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
bullets = pygame.sprite.Group()

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

bullet2_image = pygame.image.load("Bullet1.png")
bullet2_image = pygame.transform.rotozoom(bullet2_image, 90, 3)

#Hp Bar Images
bar1_image = pygame.image.load("Bar1.png")
bar1_image = pygame.transform.rotozoom(bar1_image, 0, 0.8)
bar2_image = pygame.image.load("Bar2.png")
bar2_image = pygame.transform.rotozoom(bar2_image, 0, 0.8)
bar3_image = pygame.image.load("Bar3.png")
bar3_image = pygame.transform.rotozoom(bar3_image, 0, 0.8)
bar4_image = pygame.image.load("Bar4.png")
bar4_image = pygame.transform.rotozoom(bar4_image, 0, 0.8)
bar5_image = pygame.image.load("Bar5.png")
bar5_image = pygame.transform.rotozoom(bar5_image, 0, 0.8)
bar6_image = pygame.image.load("Bar6.png")
bar6_image = pygame.transform.rotozoom(bar6_image, 0, 0.8)

#Warning Image
Warning_image = pygame.image.load("Warning.png")
Warning_image = pygame.transform.rotozoom(Warning_image, 0, 1)

#Warning Image
Warning2_image = pygame.image.load("Warning.png")
Warning2_image = pygame.transform.rotozoom(Warning_image, 0, 2)

#Restart Image
restart_image = pygame.image.load("Restart.png")
restart_image = pygame.transform.rotozoom(restart_image, 0, 0.6)

#Start Image
start_image = pygame.image.load("Restart.png")
start_image = pygame.transform.rotozoom(start_image, 0, 0.6)

#Menu Image
menu_image = pygame.image.load("Menu.png")
menu_image = pygame.transform.rotozoom(menu_image, 0, 0.6)

#-=-=-=-=-=-(Create Sprites)-=-=-=-=-=-

#Player Sprite.
player = Sprite(player1_image)
player.center = (plr_x, plr_y)
player.add(all_sprites)
player.image_num = 1
player.count = 0

#HP Sprite
HP_bar = Sprite(bar1_image)
HP_bar.center = (WIDTH / 2, 595)
HP_bar.add(all_sprites)
HP_bar.hp_num = 1

#Warning Sprite
warning = Sprite(Warning_image)
warning.counter = 0

#Big Warning Sprite
warning_big = Sprite(Warning2_image)

#Timer
baloo_font_small = pygame.font.Font("Baloo.ttf", 36)
time_left = START_TIME
timer = Sprite(baloo_font_small.render(f"{time_left}", True, FONT_COLOR))
timer.center = (590, 30)
timer.add(all_sprites)

#Game Over
baloo_font_large = pygame.font.Font("Baloo.ttf", 72)
game_over = Sprite(baloo_font_large.render("YOU ARE DEAD", True, GAME_OVER_COLOR))
game_over.center = (WIDTH / 2, HEIGHT / 2)

#You Win
baloo_font_large = pygame.font.Font("Baloo.ttf", 72)
win = Sprite(baloo_font_large.render("YOU WIN", True, GAME_OVER_COLOR))
win.center = (WIDTH / 2, HEIGHT / 2)

#Buttons
restart_button = Sprite(restart_image)
restart_button.center = (185, 405)
start_button = Sprite(start_image)
start_button.center = (100, 595)
menu_button = Sprite(menu_image)
menu_button.center = (445, 405)

#-=-=-=-=-(Sounds)-=-=-=-=-=-
win_sound = pygame.mixer.Sound("win.mp3")
warning_sound = pygame.mixer.Sound("warning.mp3")
lose_sound = pygame.mixer.Sound("lose.mp3")

#-=-=-=-=-(Bg Music)-=-=-=-=-
pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.play()

#-=-=-=-=-(Custom Events)-=-=-=-=-
SPAWNCLOCK = pygame.event.custom_type()
pygame.time.set_timer(SPAWNCLOCK, time1)

WARNING = pygame.event.custom_type()
pygame.time.set_timer(WARNING, time2)

COUNTDOWN = pygame.event.custom_type()
pygame.time.set_timer(COUNTDOWN, 1000, time_left)

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
        elif event.type == COUNTDOWN:
            time_left -= 1
            timer.image = baloo_font_small.render(f"{time_left}", True, FONT_COLOR)
            timer.center = (590, 30)
            
            if HP_bar.hp_num >= 6:
                for sprites in all_sprites:
                    timer.kill()
                    sprites.kill()
                    player.kill()
                    bullet.kill()
                game_over.add(all_sprites)
                restart_button.add(all_sprites)
                menu_button.add(all_sprites)
                pygame.mixer.music.stop()
            
            elif time_left == 0:
                win_sound.play()
                for sprites in all_sprites:
                    timer.kill()
                    sprites.kill()
                    player.kill()
                    bullet.kill()
                win.add(all_sprites)
                restart_button.add(all_sprites)
                menu_button.add(all_sprites)
                pygame.mixer.music.stop()
        
        elif event.type == MOUSEBUTTONDOWN:
            if restart_button.mask_contains_point(event.pos) and restart_button.alive():
                time_left = START_TIME
                timer.image = baloo_font_small.render(f"{time_left}", True, FONT_COLOR)
                timer.center = (590, 30)
                timer.add(all_sprites)
                restart_button.kill()
                menu_button.kill()
                game_over.kill()
                win.kill()
                player.add(all_sprites)
                HP_bar.add(all_sprites)
                pygame.time.set_timer(COUNTDOWN, 1000, time_left)
                pygame.mixer.music.rewind()
                pygame.mixer.music.play()
                HP_bar.hp_num = 1
                bullet_speed = 4
                plr_speed = 2
                warning_bullet_speed = 5
                HP_bar.image = bar1_image
                HP_bar.add(all_sprites)
                plr_x = WIDTH / 2
                plr_y = 400
        
        #-=-=-=-(Starting Attack)-=-=-=-
        if time_left == 70 or time_left == 40 or time_left == 10:
            warning_big.center = (50, 400)
            warning_big.add(all_sprites)
            warning_sound.play()
        if time_left == 69 or time_left == 39 or time_left == 9:
            warning_big.kill()
            bullet = Sprite(bullet2_image)
            bullet.center = (0, 400)
            bullet.direction = 360
            bullet.add(all_sprites, bullets)
            bullet.speed = (warning_bullet_speed)
            warning_bullet_speed += 0.3
            
        #-=-=-=-(Warning Attack)-=-=-=-
        if event.type == WARNING and player.alive():
            warning_attack = random.randint(1, 3)
            
            if warning_attack == 2 and time_left <= 68:
                y_r = random.randint(250, 500)
                warning.center = (30, y_r)
                warning.add(all_sprites)
                warning_attack = 0
                warning_sound.play(2)
                if warning_attack == 0:
                    bullet = Sprite(bullet1_image)
                    bullet.center = (0, y_r)
                    bullet.direction = 360
                    bullet.add(all_sprites, bullets)
                    bullet.speed = (warning_bullet_speed)
                    warning_bullet_speed += 0.3
                    warning.counter = 0
 
            else:
                warning.kill()
                        
        #-=-=-=-(Tracking Bullet)-=-=-=-
        if event.type == SPAWNCLOCK and player.alive():
            
            if time_left <= 68:
                y_r = random.randint(250, 500)
                bullet_speed += 0.01
                plr_speed += 0.01
                bullet = Sprite(bullet1_image)
                bullet.center = (0, y_r)
                bullet.direction = degrees(atan((y_r - player.centery) / (player.centerx - x_r)))
                bullet.add(all_sprites, bullets)
                bullet.speed = (bullet_speed)
                if time_left == 50:
                    bullet_speed += 0.2
                    plr_speed += 0.2
                    if time_left == 30:
                        bullet_speed += 0.2
                        plr_speed += 0.2
                        warning_bullet_speed += 0.5


    ### MANAGE GAME STATE FRAME-BY-FRAME
    
    #-=-=-=-=-(HP BAR)-=-=-=-=-
    for bullet in bullets:
    #If the bullet goes off the screen, wrap around to the other side of the screen
        if bullet.left > WIDTH:
            bullet.kill()
        if bullet.right < 0:
            bullet.kill()
        if bullet.top < 220:
            bullet.kill()
        if bullet.bottom > 555:
            bullet.kill()
        
        if pygame.sprite.collide_mask(player, bullet):
            HP_bar.hp_num += 1
            bullet.kill()
    
        if HP_bar.hp_num == 1 or time_left == 75:
            HP_bar.image = bar1_image
            HP_bar.add(all_sprites)
            
        elif HP_bar.hp_num == 2:
            HP_bar.kill()
            HP_bar.image = bar2_image
            HP_bar.add(all_sprites)
            
        elif HP_bar.hp_num == 3:
            HP_bar.kill()
            HP_bar.image = bar3_image
            HP_bar.add(all_sprites)
        
        elif HP_bar.hp_num == 4:
            HP_bar.kill()
            HP_bar.image = bar4_image
            HP_bar.add(all_sprites)
        
        elif HP_bar.hp_num == 5:
            HP_bar.kill()
            HP_bar.image = bar5_image
            HP_bar.add(all_sprites)
    
        elif HP_bar.hp_num == 6:
            HP_bar.kill()
            HP_bar.image = bar6_image
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
    border1 = pygame.draw.rect(screen, (255, 255, 255), (0, 220, WIDTH, 5), 0)
    border2 = pygame.draw.rect(screen, (255, 255, 255), (0, 550, WIDTH, 5), 0)

    
    # Redraw the sprites
    all_sprites.draw(screen)

    # Uncomment the next line to show a grid
    # screen.blit(grid, (0,0))

    # Flip the changes to the screen to the computer display
    pygame.display.flip()
    
# Quit the pygame program
pygame.quit()
