import math
import matplotlib.pyplot as plt
import numpy as np
from physics.body import Body
from environment.gravity import gravity_force
from control.thruster import thrust_vector

class Simulator:
    def __init__(self, config, ga, astar):
        self.config = config
        self.ga = ga
        self.astar = astar
        self.body = Body(config.START, config.INITIAL_VELOCITY)
        self.dt = config.DT

    def run(self):
        trajectory = []
        print(f"Start: ({self.config.START[0]:.2f}, {self.config.START[1]:.2f})")
        print(f"Target: ({self.config.TARGET[0]:.2f}, {self.config.TARGET[1]:.2f})")

        # Step 1: GA selects waypoint
        start_state = (
            self.body.position[0],
            self.body.position[1],
            self.body.velocity[0],
            self.body.velocity[1]
        )
        waypoint = self.ga.evolve(start_state)
        waypoint = (round(float(waypoint[0])), round(float(waypoint[1])))
        print(f"GA waypoint selected: ({waypoint[0]:.2f}, {waypoint[1]:.2f})")

        # Step 2: A* expands path
        path1 = self.astar.plan(start_state, waypoint)
        path2 = self.astar.plan((waypoint[0], waypoint[1], 0, 0), self.config.TARGET)
        full_path = path1 + path2[1:]
        print(f"A* expanded path length: {len(full_path)} nodes")

        # Step 3: Smooth path
        smoothed_path = self.smooth_path(full_path)
        smooth_more = self.smooth_path(smoothed_path)

        # Step 4: Physics execution
        for i in range(len(smooth_more)):
            target_index = min(i + self.config.LOOKAHEAD, len(smooth_more) - 1)
            target_node = smooth_more[target_index]

            dx = target_node[0] - self.body.position[0]
            dy = target_node[1] - self.body.position[1]
            dist = math.hypot(dx, dy)

            if self.body.fuel <= 1.5:
                print(" Simulation stopped: fuel exhausted.")
                return trajectory

            if dist > self.config.MAX_DISTANCE:
                print(" Force stop: satellite drifted too far.")
                return trajectory

            while dist >= 0.5 and self.body.fuel > 0:
                g = gravity_force(self.body.position)
                thrust = thrust_vector(target_node, self.body)

                fx = g[0] + 0.7 * thrust[0]
                fy = g[1] + 0.7 * thrust[1]

                self.body.apply_force((fx, fy), self.dt)
                trajectory.append((float(self.body.position[0]), float(self.body.position[1])))

                dx = target_node[0] - self.body.position[0]
                dy = target_node[1] - self.body.position[1]
                dist = math.hypot(dx, dy)

                if len(trajectory) % 50 == 0:
                    print(
                        f"Step {len(trajectory)} | "
                        f"Pos ({self.body.position[0]:.2f}, {self.body.position[1]:.2f}) | "
                        f"Vel ({self.body.velocity[0]:.2f}, {self.body.velocity[1]:.2f}) | "
                        f"Fuel {self.body.fuel:.2f}"
                    )

            print(
                f"Reached node ({target_node[0]:.2f}, {target_node[1]:.2f}) | "
                f"Vel ({self.body.velocity[0]:.2f}, {self.body.velocity[1]:.2f}) | "
                f"Fuel {self.body.fuel:.2f}"
            )

        print(
            f"\nReached target ({self.config.TARGET[0]:.2f}, {self.config.TARGET[1]:.2f}) "
            f"at ({self.body.position[0]:.2f}, {self.body.position[1]:.2f})"
        )
        print(
            f"Final velocity: ({self.body.velocity[0]:.2f}, {self.body.velocity[1]:.2f}) | "
            f"Fuel remaining: {self.body.fuel:.2f}"
        )
        return trajectory

    def smooth_path(self, path):
        xs, ys = zip(*path)
        xs = np.array(xs)
        ys = np.array(ys)

        t = np.linspace(0, 1, len(xs))
        spline_x = np.interp(np.linspace(0, 1, len(xs) * 5), t, xs)
        spline_y = np.interp(np.linspace(0, 1, len(ys) * 5), t, ys)

        return list(zip(spline_x, spline_y))

    def plot(self, trajectory):
        if not trajectory:
            print("No trajectory generated.")
            return
        xs, ys = zip(*trajectory)
        plt.figure()
        plt.plot(xs, ys, linewidth=2, label="Trajectory")
        plt.scatter(self.config.START[0], self.config.START[1], c="green", s=80, label="Start")
        plt.scatter(self.config.TARGET[0], self.config.TARGET[1], c="red", s=100, label="Target")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Smoothed GA + A* Orbit with Physics")
        plt.legend()
        plt.grid(True)
        plt.show()
