# Example file showing a circle moving on screen
import pygame
from marble import Marble

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# test objects
test_marble = Marble(40, "white", screen)

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update screen
    screen.fill("black")
    test_marble.draw()

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

# def redraw_screen():
#     screen.fill("black")
#     test_marble.draw()