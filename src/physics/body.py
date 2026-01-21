# physics/body.py
import math
from simulation.config import DT, MASS, FUEL_COST_PER_THRUST
from environment.gravity import gravity_accel

class Body:
    def __init__(self, x, y, vx, vy, fuel):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.fuel = fuel
        self.path = []

    def step(self, ax, ay):
        if self.fuel <= 0:
            ax = ay = 0.0

        # Gravity
        gx, gy = gravity_accel(self.x, self.y)

        # Acceleration
        ax_total = ax + gx
        ay_total = ay + gy

        # Integrate velocity
        self.vx += ax_total * DT
        self.vy += ay_total * DT

        # Integrate position
        self.x += self.vx * DT
        self.y += self.vy * DT

        # Fuel
        thrust_mag = math.hypot(ax, ay)
        self.fuel -= thrust_mag * FUEL_COST_PER_THRUST

        self.path.append((self.x, self.y))
