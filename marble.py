import pygame
from pygame import gfxdraw # antialiased shapes
import random

INIT_VEL_SCALAR = 150
GRAVITY_VECTOR = pygame.Vector2(0, 100)

class Marble:
    all_marbles = []
    
    def __init__(self, radius, color_fill, screen:pygame.Surface):
        Marble.all_marbles.append(self) # Append the instance to the class-level list
        
        self.radius = radius
        self.outline_width = 3
        self.color_fill = color_fill
        self.color_outline = pygame.Color("black")
        self.screen = screen

        #initial position and velocity
        self.pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.vel = pygame.Vector2(random.uniform(-INIT_VEL_SCALAR, INIT_VEL_SCALAR), random.uniform(-INIT_VEL_SCALAR, INIT_VEL_SCALAR))

        self.draw()

    def __repr__(self):
        return f"Marble({self.radius}, {self.color_fill}, {self.screen})"
    def __str__(self):
        return f"Marble, rad {self.radius}, bg_color {self.color_fill})"

    def draw(self):
        x_pos_px = int(self.pos.x)
        y_pos_px = int(self.pos.y)

        # Outline
        gfxdraw.aacircle(self.screen, x_pos_px, y_pos_px, self.radius + self.outline_width, self.color_outline)
        gfxdraw.filled_circle(self.screen, x_pos_px, y_pos_px, self.radius + self.outline_width, self.color_outline)
        
        # Fill
        gfxdraw.aacircle(self.screen, x_pos_px, y_pos_px, self.radius, self.color_fill)
        gfxdraw.filled_circle(self.screen, x_pos_px, y_pos_px, self.radius, self.color_fill)

    def update_position(self, dt):
        self.pos += (self.vel * dt)

        #check for wall collisions
        scr_width = self.screen.get_width()
        scr_height = self.screen.get_height()

        if (self.pos.x + self.radius) > scr_width:
            self.pos.x = scr_width - self.radius
            self.vel.x *= -1
        elif (self.pos.x - self.radius) < 0:
            self.pos.x = self.radius
            self.vel.x *= -1
        if (self.pos.y + self.radius) > scr_height:
            self.pos.y = scr_height - self.radius
            self.vel.y *= -1
        elif (self.pos.y - self.radius) < 0:
            self.pos.y = self.radius
            self.vel.y *= -1
    
    def update_velocity(self, dt):
        self.vel += (GRAVITY_VECTOR * dt)
