import pygame

# functions
def redraw_screen(screen:pygame.Surface, obj_list):
    screen.fill("white")
    for obj in obj_list:
        obj.draw(screen)

def render_text(text, font:pygame.Font, screen:pygame.Surface, x, y, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))