from os.path import join

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

# import an image
path = join('images', 'player.png')
player_surf = pygame.image.load(path).convert_alpha()

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += 0.1

    # draw the game
    display_surface.fill('darkgrey')
    display_surface.blit(player_surf, (x, 150))
    pygame.display.update()

pygame.quit()
