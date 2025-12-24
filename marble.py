import pygame
from pygame import gfxdraw # antialiased shapes
from pygame import Vector2 as Vec
import random

INIT_VEL_SCALAR = 250
GRAVITY_VECTOR = Vec(0, 500)

class Marble:
    all_marbles = []
    elasticity = 0.96
    gravity = 1.0
    
    def __init__(self, screen:pygame.Surface, radius=None, color_fill=None, pos=None):
        Marble.all_marbles.append(self) # Append the instance to the class-level list
        self.screen = screen

        if radius is None:
            self.radius = random.randrange(10,100)
        else:
            self.radius = radius

        if color_fill is None:
            self.color_fill = pygame.Color(random.randrange(256),random.randrange(256),random.randrange(256))
        else:
            self.color_fill = color_fill

        self.mass = 10 * self.radius * self.radius
        self.outline_width = 3
        self.color_outline = pygame.Color("black")

        #initial position and velocity
        if pos is None:
            self.pos = Vec(random.randint(self.radius, self.screen.get_width() - self.radius),
                                  random.randint(self.radius, self.screen.get_height() - self.radius))
        else: 
            self.pos = pos
        self.vel = Vec(random.uniform(-INIT_VEL_SCALAR, INIT_VEL_SCALAR), 
                                  random.uniform(-INIT_VEL_SCALAR, INIT_VEL_SCALAR))

        self.draw(self.screen)

    def __repr__(self):
        return f"Marble({self.radius}, {self.color_fill}, {self.screen})"
    def __str__(self):
        return f"Marble, rad {self.radius}, bg_color {self.color_fill})"

    def draw(self, screen:pygame.Surface):
        x_pos_px = int(self.pos.x)
        y_pos_px = int(self.pos.y)

        # Outline
        gfxdraw.aacircle(screen, x_pos_px, y_pos_px, self.radius + self.outline_width, self.color_outline)
        gfxdraw.filled_circle(screen, x_pos_px, y_pos_px, self.radius + self.outline_width, self.color_outline)
        
        # Fill
        gfxdraw.aacircle(screen, x_pos_px, y_pos_px, self.radius, self.color_fill)
        gfxdraw.filled_circle(screen, x_pos_px, y_pos_px, self.radius, self.color_fill)

    def kill(self):
        Marble.all_marbles.remove(self)

    def update_position(self, dt):
        self.pos += (self.vel * dt)
    
    def update_velocity(self, dt):
        self.vel += (Vec(0, 500 * Marble.gravity) * dt)

    def update_color(self):
        value = min(255, int(255 * self.vel.magnitude()/(INIT_VEL_SCALAR*4)))
        self.color_fill = pygame.Color(value,0,255-value)

    #simple, mass-less bounce
    def bounce(self, normal:Vec):
        normal = normal.normalize() #ensure normal vector is normalized; could be slow
        self.vel = self.vel - (self.elasticity + 1) * (self.vel.dot(normal)) * normal

