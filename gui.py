import pygame
from pygame import gfxdraw # antialiased shapes

#TODO create color pallete gallery list

class Slider:
    def __init__(self, x, y, w, min_val, max_val, start_val):
        self.rect = pygame.Rect(x, y, w, 6)   # track
        self.min_val = min_val
        self.max_val = max_val

        self.knob_radius = 8
        self.knob_outline_px = 2
        self.knob_fill = (80,80,80)
        self.dragging = False

        # initial knob position
        self.value = start_val
        self.knob_x = self.value_to_pos(start_val)

    def value_to_pos(self, value):
        t = (value - self.min_val) / (self.max_val - self.min_val)
        return int(self.rect.x + t * self.rect.w)

    def pos_to_value(self, x):
        t = (x - self.rect.x) / self.rect.w
        t = max(0.0, min(1.0, t))
        return self.min_val + t * (self.max_val - self.min_val)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if abs(event.pos[0] - self.knob_x) <= self.knob_radius:
                self.dragging = True
                self.knob_fill = (255,0,0)

        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
            self.knob_fill = (80,80,80)

        elif event.type == pygame.MOUSEMOTION and self.dragging:
            x = max(self.rect.left, min(event.pos[0], self.rect.right))
            self.knob_x = x
            self.value = self.pos_to_value(x)

    def draw(self, screen):
        # track
        pygame.draw.rect(screen, (180, 180, 180), self.rect)
        # knob
        pygame.draw.circle(
            screen, (80, 80, 80),
            (self.knob_x, self.rect.centery),
            self.knob_radius
        )

        # Knob Outline
        gfxdraw.aacircle(screen, self.knob_x, self.rect.centery, self.knob_radius + self.knob_outline_px, (0,0,0))
        gfxdraw.filled_circle(screen, self.knob_x, self.rect.centery, self.knob_radius + self.knob_outline_px, (0,0,0))
        
        # Fill
        gfxdraw.aacircle(screen, self.knob_x, self.rect.centery, self.knob_radius, self.knob_fill)
        gfxdraw.filled_circle(screen, self.knob_x, self.rect.centery, self.knob_radius, self.knob_fill)