# physics/gravity.py
import math
from simulation.config import GRAVITY_MU, PLANET_POS

def gravity_accel(x, y):
    px, py = PLANET_POS
    dx = px - x
    dy = py - y
    r2 = dx*dx + dy*dy + 1e-6
    r = math.sqrt(r2)
    a = GRAVITY_MU / r2
    return a * dx / r, a * dy / r
