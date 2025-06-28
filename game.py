import pygame
import sys
import os

# Set the desired position for the window (x, y)
os.environ['SDL_VIDEO_WINDOW_POS'] = '0, 30'

# Initialize PyGame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((1290, 690))
screen_width, screen_height = screen.get_size()
pygame.display.set_caption("Game")

# Set the frame rate
clock = pygame.time.Clock()

# Player settings
player_width = 50
player_height = 60
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5
player_angle = 0
player_image = pygame.image.load('boy_character.png')
player_rect = player_image.get_rect()
player_rect.topleft= (100, 100)
# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Draw the character on the screen
    screen.blit(player_image, player_rect)
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed
    pygame.display.update()
    screen.fill((255, 255, 255)) # Fill the screen with black
    clock.tick(60)  # Cap the frame rate at 60 FPS



