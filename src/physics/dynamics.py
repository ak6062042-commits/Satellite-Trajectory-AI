def compute_acceleration(body, force):
    return (force[0] / body.mass, force[1] / body.mass)
