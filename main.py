import pygame, random

# Set display surface
pygame.init()

# Set display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed The Dragon")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set game value:  CONSTANT_NAME, value
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY = 10
COIN_ACCELERATION = 0.5
BUFFER_DISTANCE = 100
#YOU do the remaining 4 CONSTANTS

#Set Game Variables:  variable_name
' 3 variables'
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY
score = 0
#YOU do the remaining 2 variables

#Set colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Set fonts
font = pygame.font.Font('AttackGraffiti.ttf', 32)

#Set Text for Score


score_text = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

#Set Text for Title (Similar to Score)

title_text = font.render("FEED THY DRAGON", True, GREEN, DARKGREEN)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH // 2
title_rect.y = 10


lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARKGREEN)
lives_rect = score_text.get_rect()
lives_rect.topright= (980, 10)
#Set Text for Game Over (Similar to Score)

center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
game_over_text = font.render("ez your horrid", True, GREEN, DARKGREEN)
game_over_rect = center

#Set Text for Continue (Similar to Score)
'''
variable names:  continue_text, continue_rect  
render text: "Press any key to play again"
antialias: True
color: GREEN
background: DARKGREEN
rect location: center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 32)
'''
coin_sound = pygame.mixer.Sound("coin_sound.wav")
coin_sound.set_volume(0.2)
miss_sound = pygame.mixer.Sound("miss_sound.wav")
miss_sound.set_volume(0.5)
pygame.mixer.music.load("ftd_background_music.wav")


player_image = pygame.image.load("dragon_right.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT //2





pygame.mixer.music.play(-1, 0.0, 4)





# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fill the display
    display_surface.fill(BLACK)

    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(player_image, player_rect)

    #Update display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()