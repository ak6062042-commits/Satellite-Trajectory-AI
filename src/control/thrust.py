import math

MAX_THRUST = 18.0
FUEL_RATE = 0.03

def thrust_vector(target, body):
    if body.fuel <= 0:
        return (0.0, 0.0)

    dx = target[0] - body.position[0]
    dy = target[1] - body.position[1]

    vx, vy = body.velocity

    dist = math.hypot(dx, dy)
    speed = math.hypot(vx, vy)

    if dist > 1e-6:
        dx /= dist
        dy /= dist

    tx = dx - 0.9 * vx
    ty = dy - 0.9 * vy

    mag = math.hypot(tx, ty)
    if mag < 1e-6:
        return (0.0, 0.0)

    tx /= mag
    ty /= mag

    thrust = MAX_THRUST
    if dist < 30:
        thrust *= 0.5
    if dist < 10:
        thrust *= 0.2

    fuel_cost = thrust * FUEL_RATE
    if body.fuel < fuel_cost:
        thrust *= body.fuel / fuel_cost
        fuel_cost = body.fuel

    body.fuel -= fuel_cost
    return (tx * thrust, ty * thrust)
