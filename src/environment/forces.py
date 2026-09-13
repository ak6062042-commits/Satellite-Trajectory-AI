from utils.utils import magnitude


def drag_force(velocity, coefficient=0.0):
    speed = magnitude(velocity)
    if coefficient <= 0 or speed == 0:
        return (0.0, 0.0)
    return (-coefficient * speed * velocity[0], -coefficient * speed * velocity[1])


def solar_pressure_force(direction=(1.0, 0.0), magnitude_value=0.0):
    length = magnitude(direction)
    if magnitude_value == 0 or length == 0:
        return (0.0, 0.0)
    return (magnitude_value * direction[0] / length, magnitude_value * direction[1] / length)
