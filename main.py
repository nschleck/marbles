# Example file showing a circle moving on screen
import pygame
from pygame import gfxdraw # antialiasing
from marble import Marble
from render import *
from solver import *


from itertools import combinations

# TODO implement sprites
# TODO implement iterative marble un-overlapper?
# TODO group Marble objects in special Marbles class instance? w/ functions
# TODO implement blur trails
    
# pygame setup
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Arial", 18, bold=True)
pygame.display.set_caption('marbels')
pygame.display.set_icon(pygame.image.load('graphics/window_icon.png'))
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# test objects
test_marble = Marble(40, pygame.Color("purple"), screen)
test_marble_2 = Marble(30, pygame.Color("red"), screen)
test_marble_3 = Marble(50, pygame.Color("blue"), screen)
test_marble_4 = Marble(10, pygame.Color("yellow"), screen)

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            click_x, click_y = event.pos # event.pos returns a tuple (x, y)
            newMarble = Marble(30, pygame.Color("purple"), screen, pos=pygame.Vector2(click_x,click_y))
            #print(f"Mouse clicked at x: {click_x}, y: {click_y}")

    # update screen
    redraw_screen(screen, Marble.all_marbles)

    # update physics
    for marble in Marble.all_marbles:
        marble.update_position(dt)
        marble.update_velocity(dt) #also checks for wall bounces
    
    # do collisions between marble pairs
    for marbleA, marbleB in combinations(Marble.all_marbles, 2):
        AB_offset = pygame.Vector2(marbleB.pos - marbleA.pos)
        bounce_distance = marbleB.radius + marbleA.radius

        if (AB_offset.magnitude() <= bounce_distance):
            resolve_marble_collision(marbleA, marbleB)

    #keys = pygame.key.get_pressed()

    # Get FPS value as a string and render it
    fps_value = str(int(clock.get_fps()))
    fps_surface = font.render(fps_value, True, (255, 0, 0)) # Red color
    screen.blit(fps_surface, (10, 10)) # Position at top left

    pygame.display.flip()

    dt = clock.tick() / 1000 # optionality to limit FPS to 60

pygame.quit()