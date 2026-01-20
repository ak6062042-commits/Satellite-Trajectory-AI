import math

def thrust_vector(target, body):
    if body.fuel <= 0:
        return (0.0, 0.0)

    dx = target[0] - body.position[0]
    dy = target[1] - body.position[1]
    dist = math.hypot(dx, dy)

    if dist < 0.5:
        return (0.0, 0.0)

    ux, uy = dx / dist, dy / dist
    desired_speed = max(1.0, min(6.0, dist / 10.0))
    desired_vx = ux * desired_speed
    desired_vy = uy * desired_speed

    ax = desired_vx - body.velocity[0]
    ay = desired_vy - body.velocity[1]

    mag = math.hypot(ax, ay)
    if mag < 0.1:
        return (0.0, 0.0)

    max_thrust = 4.0
    if mag > max_thrust:
        ax, ay = (ax / mag) * max_thrust, (ay / mag) * max_thrust
        mag = max_thrust

    fuel_cost = 0.5 * mag
    if body.fuel < fuel_cost:
        return (0.0, 0.0)

    body.fuel -= fuel_cost
    return (ax, ay)
