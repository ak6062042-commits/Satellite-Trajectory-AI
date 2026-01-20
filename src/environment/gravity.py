import math

MU = 2000.0

def gravity_force(position):
    x, y = position
    r2 = x*x + y*y
    if r2 == 0:
        return (0.0, 0.0)
    r = math.sqrt(r2)
    g = -MU / r2
    return (g * x / r, g * y / r)
