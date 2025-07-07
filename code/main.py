from os.path import join
from random import randint

import pygame

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
running = True

# create display surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# set the title of the window
pygame.display.set_caption('Space Shooter')

# plain surface
surf = pygame.Surface((100, 200))
surf.fill('orange')
x = 100

# import an image for the player
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
x_forwards = True

# import star
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill('darkgrey')
    for i in range(20):
        display_surface.blit(star_surf, star_positions[i])
    display_surface.blit(player_surf, (x, 150))
    pygame.display.update()

pygame.quit()
