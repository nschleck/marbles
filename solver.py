from marble import Marble

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