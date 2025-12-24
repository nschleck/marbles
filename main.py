# Example file showing a circle moving on screen
import pygame
#from pygame import gfxdraw # antialiasing
from itertools import combinations

from marble import Marble
from render import *
from solver import *
from gui import *
from utils import *

# TODO make gui objects scalable
# TODO fix slider linking bug
# TODO implement reset button
# TODO implement pause, play, setp forward buttons?
# TODO implement iterative marble un-overlapper?

# TODO group Marble objects in special Marbles class instance? w/ functions?
# TODO implement blur trails
# TODO implement sprites?
    
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

# gui
slider_elasticity = Slider(
    x=10,
    y=70,
    w=300,
    min_val=0.0,
    max_val=1.0,
    start_val=1.0
)

slider_gravity = Slider(
    x=10,
    y=130,
    w=300,
    min_val=0.0,
    max_val=10.0,
    start_val=1.0
)

# test objects
test_marble = Marble(screen, 40)
test_marble_2 = Marble(screen, 30)
test_marble_3 = Marble(screen, 50)
test_marble_4 = Marble(screen, 10)

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif (event.type == pygame.MOUSEBUTTONUP) and not slider_elasticity.dragging and not slider_gravity.dragging:
            click_x, click_y = event.pos
            newMarble = Marble(screen, pos=pygame.Vector2(click_x,click_y))
            #report_xy(click_x, click_y)
        slider_elasticity.handle_event(event)
        slider_gravity.handle_event(event)

    # update screen
    redraw_screen(screen, Marble.all_marbles)

    # update physics
    for marble in Marble.all_marbles:
        marble.update_position(dt)
        marble.update_velocity(dt)
        marble.update_color()
    
    # do collisions between marble pairs and walls
    for marble in Marble.all_marbles:
        resolve_wall_collision(marble)

    for marbleA, marbleB in combinations(Marble.all_marbles, 2):
        AB_offset = pygame.Vector2(marbleB.pos - marbleA.pos)
        bounce_distance = marbleB.radius + marbleA.radius

        if (AB_offset.magnitude() <= bounce_distance):
            resolve_marble_collision(marbleA, marbleB)

    # update elasticity and gravity sliders and render
    Marble.elasticity = slider_elasticity.value
    slider_elasticity.draw(screen)
    slider_text = font.render(f"Elasticity: {slider_elasticity.value:.2f}", True, (0, 0, 0))
    screen.blit(slider_text, (slider_elasticity.rect.x, slider_elasticity.rect.y - 25))

    Marble.gravity = slider_gravity.value
    slider_gravity.draw(screen)
    slider_text = font.render(f"Gravity: {slider_gravity.value:.2f}", True, (0, 0, 0))
    screen.blit(slider_text, (slider_gravity.rect.x, slider_gravity.rect.y - 25))   

    # Get FPS value as a string and render it
    fps_value = "FPS:" + str(int(clock.get_fps()))
    render_text(fps_value, font, screen, 10, 10, (0,0,0))

    pygame.display.flip()

    dt = clock.tick() / 1000 # optionality to limit FPS to 60

pygame.quit()