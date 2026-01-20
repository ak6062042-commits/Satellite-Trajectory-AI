class Body:
    def __init__(self, position, velocity, mass=1.0, fuel=300.0):
        self.position = [float(position[0]), float(position[1])]
        self.velocity = [float(velocity[0]), float(velocity[1])]
        self.mass = mass
        self.fuel = fuel

    def apply_force(self, force, dt):
        ax = force[0] / self.mass
        ay = force[1] / self.mass
        self.velocity[0] += ax * dt
        self.velocity[1] += ay * dt
        self.position[0] += self.velocity[0] * dt
        self.position[1] += self.velocity[1] * dt
