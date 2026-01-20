import math

MAX_THRUST = 25.0          
FUEL_RATE = 0.03           

def thrust_vector(target, body):
    if body.fuel <= 0:
        return (0.0, 0.0)

    tx = target[0] - body.position[0]
    ty = target[1] - body.position[1]

    dist = math.hypot(tx, ty)
    if dist < 1e-3:
        return (0.0, 0.0)

    # Direction to target
    dx = tx / dist
    dy = ty / dist

    speed = math.hypot(body.velocity[0], body.velocity[1])

    # Braking near target
    if dist < 25:
        dx = -body.velocity[0]
        dy = -body.velocity[1]
        mag = math.hypot(dx, dy)
        if mag > 1e-6:
            dx /= mag
            dy /= mag
        thrust = MAX_THRUST * 1.3   # stronger braking
    else:
        thrust = MAX_THRUST

    body.fuel -= FUEL_RATE * thrust
    return (dx * thrust, dy * thrust)
