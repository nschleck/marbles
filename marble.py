import pygame
from pygame import gfxdraw # antialiased shapes

class Marble:
  def __init__(self, radius, color_fill, screen:pygame.Surface):
    #self.x_pos = x_pos
    #self.y_pos = y_pos
    self.radius = radius
    self.outline_width = 3
    self.color_fill = color_fill
    self.color_outline = pygame.Color("black")
    self.screen = screen
    self.pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
    self.draw()

  def draw(self):
    x_pos_px = int(self.pos.x)
    y_pos_px = int(self.pos.y)

    # Outline
    gfxdraw.aacircle(self.screen, x_pos_px, y_pos_px, self.radius + self.outline_width, self.color_outline)
    gfxdraw.filled_circle(self.screen, x_pos_px, y_pos_px, self.radius + self.outline_width, self.color_outline)
    
    # Fill
    gfxdraw.aacircle(self.screen, x_pos_px, y_pos_px, self.radius, self.color_fill)
    gfxdraw.filled_circle(self.screen, x_pos_px, y_pos_px, self.radius, self.color_fill)
    