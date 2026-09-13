import math

from utils.utils import magnitude


class Thruster:
    def __init__(self, max_force=6.0, fuel_rate=0.12, velocity_gain=1.8, max_speed=10.0):
        self.max_force = float(max_force)
        self.fuel_rate = float(fuel_rate)
        self.velocity_gain = float(velocity_gain)
        self.max_speed = float(max_speed)

    def command(self, target, body, dt):
        if body.fuel <= 0 or dt <= 0:
            return (0.0, 0.0)
        dx = target[0] - body.position[0]
        dy = target[1] - body.position[1]
        distance = math.hypot(dx, dy)
        if distance < 1e-9:
            desired_velocity = (0.0, 0.0)
        else:
            speed = min(self.max_speed, distance * 0.8)
            desired_velocity = (dx * speed / distance, dy * speed / distance)
        force = (
            body.mass * self.velocity_gain * (desired_velocity[0] - body.velocity[0]),
            body.mass * self.velocity_gain * (desired_velocity[1] - body.velocity[1]),
        )
        force_size = magnitude(force)
        if force_size > self.max_force:
            scale = self.max_force / force_size
            force = (force[0] * scale, force[1] * scale)
            force_size = self.max_force
        required_fuel = force_size * self.fuel_rate * dt
        if required_fuel > body.fuel and required_fuel > 0:
            scale = body.fuel / required_fuel
            force = (force[0] * scale, force[1] * scale)
            required_fuel = body.fuel
        body.burn_fuel(required_fuel)
        return force


def thrust_vector(target, body, max_force=6.0):
    dx = target[0] - body.position[0]
    dy = target[1] - body.position[1]
    distance = math.hypot(dx, dy)
    if distance < 1e-9 or body.fuel <= 0:
        return (0.0, 0.0)
    scale = max_force / distance
    return (dx * scale, dy * scale)
