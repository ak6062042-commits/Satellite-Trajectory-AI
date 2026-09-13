def euler_step(body, acceleration, dt):
    if dt <= 0:
        raise ValueError("dt must be positive")
    body.velocity[0] += acceleration[0] * dt
    body.velocity[1] += acceleration[1] * dt
    body.position[0] += body.velocity[0] * dt
    body.position[1] += body.velocity[1] * dt
    return body
