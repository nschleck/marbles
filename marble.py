import pygame

class Marble:
  def __init__(self, radius, color, screen:pygame.Surface):
    #self.x_pos = x_pos
    #self.y_pos = y_pos
    self.radius = radius
    self.color  = color
    self.screen = screen

    self.pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
    pygame.draw.circle(self.screen, self.color, self.pos, self.radius)

  def draw(self):
    pygame.draw.circle(self.screen, self.color, self.pos, self.radius)