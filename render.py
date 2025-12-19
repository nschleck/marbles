import pygame

# functions
def redraw_screen(screen:pygame.Surface, obj_list):
    screen.fill("white")
    for obj in obj_list:
        obj.draw()