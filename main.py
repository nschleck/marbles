# Example file showing a circle moving on screen
import pygame
from pygame import gfxdraw # antialiasing
from marble import Marble
from render import *

from itertools import combinations

# TODO implement sprites
# TODO group Marble objects in special Marbles class instance? w/ functions
# TODO implement blur trails

# functions
def resolve_marble_collision(objA:Marble, objB:Marble):
    normal = (objA.pos-objB.pos).normalize()
    vel_relative = objA.vel - objB.vel
    vel_rel_n = vel_relative.dot(normal)

    if(vel_rel_n > 0):
        return #no collision
    
    j = -(1 + Marble.elasticity) * vel_rel_n / (1/objA.mass + 1/objB.mass)

    objA.vel = objA.vel + (j / objA.mass) * normal
    objB.vel = objB.vel - (j / objB.mass) * normal
    
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# test objects
test_marble = Marble(40, pygame.Color("purple"), screen)
test_marble_2 = Marble(30, pygame.Color("red"), screen)
test_marble_3 = Marble(50, pygame.Color("blue"), screen)

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
            # marbleA.bounce(-AB_offset.normalize(), (marbleB.mass/marbleA.mass))
            # marbleB.bounce(AB_offset.normalize(), (marbleA.mass/marbleB.mass))
            resolve_marble_collision(marbleA, marbleB)

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