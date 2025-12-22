from marble import Marble
from pygame import Vector2 as Vec

# functions
def resolve_marble_collision(objA:Marble, objB:Marble):
    normal = (objA.pos-objB.pos).normalize()
    vel_relative = objA.vel - objB.vel
    vel_rel_n = vel_relative.dot(normal)

    if(vel_rel_n > 0):
        return #no collision
    
    j = -(1 + Marble.elasticity) * vel_rel_n / (1/objA.mass + 1/objB.mass)

    objA.vel = objA.vel + (j / objA.mass) * normal
    objB.vel = objB.vel - (j / objB.mass) * normal

def resolve_wall_collision(marble:Marble):
        scr_width = marble.screen.get_width()
        scr_height = marble.screen.get_height()

        if (marble.pos.x + marble.radius) > scr_width:
            marble.pos.x = scr_width - marble.radius
            marble.bounce(Vec(-1,0))
        elif (marble.pos.x - marble.radius) < 0:
            marble.pos.x = marble.radius
            marble.bounce(Vec(1,0))
        if (marble.pos.y + marble.radius) > scr_height:
            marble.pos.y = scr_height - marble.radius
            marble.bounce(Vec(0,-1))
        elif (marble.pos.y - marble.radius) < 0:
            marble.pos.y = marble.radius
            marble.bounce(Vec(0,1))