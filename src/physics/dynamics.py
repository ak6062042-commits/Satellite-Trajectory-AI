def compute_acceleration(body, force):
    return (force[0] / body.mass, force[1] / body.mass)


def add_forces(*forces):
    return (
        sum(force[0] for force in forces),
        sum(force[1] for force in forces),
    )
