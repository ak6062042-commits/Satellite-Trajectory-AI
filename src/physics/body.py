class Body:
    def __init__(self, position, velocity, mass=1.0, fuel=10000.0):
        self.position = [float(position[0]), float(position[1])]
        self.velocity = [float(velocity[0]), float(velocity[1])]
        self.mass = mass
        self.fuel = fuel

    def step(self, force, dt):
        self.velocity[0] += force[0] * dt
        self.velocity[1] += force[1] * dt
        self.position[0] += self.velocity[0] * dt
        self.position[1] += self.velocity[1] * dt
