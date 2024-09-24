import pygame, random

# Set display surface
pygame.init()

# Set display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed The Dragon")

FPS = 60
clock = pygame.time.Clock()

PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY = 10
COIN_ACCELERATION = 0.5
BUFFER_DISTANCE = 100
# YOU do the remaining 4 CONSTANTS

# Set Game Variables:  variable_name
' 3 variables'
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY
score = 0

GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
gold = (255, 215, 0)

font = pygame.font.Font('AttackGraffiti.ttf', 32)

score_text = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

title_text = font.render("FEED THY DRAGON", True, GREEN, DARKGREEN)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH // 2
title_rect.y = 10

lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARKGREEN)
lives_rect = score_text.get_rect()
lives_rect.topright = (980, 10)
# Set Text for Game Over (Similar to Score)


game_over_text = font.render("ez your horrid", True, GREEN, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect = (400, 200)

continue_text = font.render("press any key to play again", True, GREEN, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect = (300, 200)

coin_sound = pygame.mixer.Sound("coin_sound.wav")
coin_sound.set_volume(0.2)
miss_sound = pygame.mixer.Sound("miss_sound.wav")
miss_sound.set_volume(0.5)
pygame.mixer.music.load("ftd_background_music.wav")

coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.centerx = WINDOW_HEIGHT + BUFFER_DISTANCE
coin_rect.centery = random.randint(64, WINDOW_HEIGHT - 32)

player_image = pygame.image.load("dragon_right.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT // 2

pygame.mixer.music.play(-1, 0.0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check to see if the user wants to move.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.y > 64:
        player_rect.y -= PLAYER_VELOCITY
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += PLAYER_VELOCITY

    # Move the coin
    if coin_rect.x < 0:
        # Player missed the coin
        player_lives -= 1
        miss_sound.play()
        coin_rect.centerx = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.centery = random.randint(64, WINDOW_HEIGHT - 32)
    else:
        # Move the Coin
        coin_rect.x -= coin_velocity

    # Check for collisions
    if player_rect.colliderect(coin_rect):
        score += 1
        coin_sound.play()
        coin_velocity += COIN_ACCELERATION
        coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
        coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

        score_text = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
        lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARKGREEN)

    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                # The player wants to play again
                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    player_rect.y = WINDOW_HEIGHT // 2
                    coin_velocity = COIN_STARTING_VELOCITY
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

                    # Fill the display


    display_surface.fill(BLACK)

    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(player_image, player_rect)
    display_surface.blit(coin_image, coin_rect)
    pygame.draw.line(display_surface, WHITE, (0,64),(WINDOW_WIDTH, 64), 2)

    # Update display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
