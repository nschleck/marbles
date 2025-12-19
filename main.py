# Example file showing a circle moving on screen
import pygame
from pygame import gfxdraw # antialiasing
from marble import Marble
from render import *

# TODO implement sprites
# TODO implement physics
# TODO implement sprite-based phyics collisions


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# test objects
marbles = []
test_marble = Marble(40, pygame.Color("purple"), screen)
test_marble_2 = Marble(30, pygame.Color("red"), screen)
marbles.append(test_marble)
marbles.append(test_marble_2)

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update screen
    redraw_screen(screen, marbles)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        test_marble.pos.y -= 300 * dt
    if keys[pygame.K_s]:
        test_marble.pos.y += 300 * dt
    if keys[pygame.K_a]:
        test_marble.pos.x -= 300 * dt
    if keys[pygame.K_d]:
        test_marble.pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # limits FPS to 60

pygame.quit()