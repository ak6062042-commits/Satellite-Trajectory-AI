import math


def gravity_force(position, source=(0.0, 0.0), mu=2000.0, mass=1.0, softening=1.0):
    dx = source[0] - position[0]
    dy = source[1] - position[1]
    distance_squared = dx * dx + dy * dy + softening * softening
    distance = math.sqrt(distance_squared)
    scale = mass * mu / (distance_squared * distance)
    return (scale * dx, scale * dy)
