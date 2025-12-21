import pygame
from pygame import gfxdraw # antialiased shapes
from pygame import Vector2 as Vec
import random

INIT_VEL_SCALAR = 250
GRAVITY_VECTOR = Vec(0, 500)

class Marble:
    all_marbles = []
    elasticity = 1
    
    def __init__(self, radius, color_fill, screen:pygame.Surface):
        Marble.all_marbles.append(self) # Append the instance to the class-level list
        
        self.radius = radius
        self.mass = 10 * radius * radius
        self.outline_width = 3
        self.color_fill = color_fill
        self.color_outline = pygame.Color("black")
        self.screen = screen

        #initial position and velocity
        self.pos = Vec(random.randint(self.radius, self.screen.get_width() - self.radius),
                                  random.randint(self.radius, self.screen.get_height() - self.radius))
        self.vel = Vec(random.uniform(-INIT_VEL_SCALAR, INIT_VEL_SCALAR), 
                                  random.uniform(-INIT_VEL_SCALAR, INIT_VEL_SCALAR))

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
            self.bounce(Vec(-1,0), 1)
        elif (self.pos.x - self.radius) < 0:
            self.pos.x = self.radius
            self.bounce(Vec(1,0), 1)
        if (self.pos.y + self.radius) > scr_height:
            self.pos.y = scr_height - self.radius
            self.bounce(Vec(0,-1), 1)
        elif (self.pos.y - self.radius) < 0:
            self.pos.y = self.radius
            self.bounce(Vec(0,1), 1)
    
    def update_velocity(self, dt):
        self.vel += (GRAVITY_VECTOR * dt)

    def bounce(self, normal:Vec, massRatio):
        normal = normal.normalize() #ensure normal vector is normalized; could be slow
        massFactor = 2 * massRatio / (1 + massRatio)
        self.vel = self.vel - (self.elasticity + 1) * (self.vel.dot(normal)) * normal * massFactor

