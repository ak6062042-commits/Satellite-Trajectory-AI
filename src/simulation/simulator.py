import matplotlib.pyplot as plt
import math
from physics.body import Body
from environment.gravity import gravity_force
from control.thrust import thrust_vector
from environment.space import Space

class Simulator:
    def __init__(self, config, ga, astar):
        self.config = config
        self.ga = ga
        self.astar = astar
        self.body = Body(config.START, config.INITIAL_VELOCITY)
        self.space = Space(config.TARGET)
        self.dt = config.DT

    def run(self):
        traj = []
        step = 0

        print(f"START pos=({self.body.position[0]:.2f},{self.body.position[1]:.2f}) "
              f"fuel={self.body.fuel:.2f}")

        while step < self.config.STEPS:
            speed = math.hypot(self.body.velocity[0], self.body.velocity[1])

            if self.body.fuel <= 0:
                print("TERMINATED: fuel exhausted")
                break

            if speed > 30:
                print("TERMINATED: unstable velocity")
                break

            state = (
                self.body.position[0],
                self.body.position[1],
                self.body.velocity[0],
                self.body.velocity[1]
            )

            waypoint = self.ga.evolve(state)
            target = self.astar.plan(state, waypoint, gravity_force)

            g = gravity_force(self.body.position)
            thrust = thrust_vector(target, self.body)

            fx = g[0] + thrust[0]
            fy = g[1] + thrust[1]

            prev_fuel = self.body.fuel
            self.body.step((fx, fy), self.dt)

            traj.append((self.body.position[0], self.body.position[1]))

            dist = math.hypot(
                self.body.position[0] - self.config.TARGET[0],
                self.body.position[1] - self.config.TARGET[1]
            )

            print(
                f"STEP {step:04d} "
                f"pos=({self.body.position[0]:.2f},{self.body.position[1]:.2f}) "
                f"vel={speed:.2f} "
                f"fuel_used={(prev_fuel - self.body.fuel):.3f} "
                f"fuel_left={self.body.fuel:.2f} "
                f"dist={dist:.2f}"
            )

            if self.space.captured(self.body.position, self.body.velocity):
                print("TARGET CAPTURED")
                break

            step += 1

        return traj

    def plot(self, traj):
        if not traj:
            print("No trajectory")
            return
        xs, ys = zip(*traj)
        plt.figure(figsize=(7,7))
        plt.plot(xs, ys)
        plt.scatter(self.config.START[0], self.config.START[1])
        plt.scatter(self.config.TARGET[0], self.config.TARGET[1])
        plt.grid(True)
        plt.show()
