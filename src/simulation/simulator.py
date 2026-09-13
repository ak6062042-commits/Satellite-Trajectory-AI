import math

import matplotlib.pyplot as plt

from control.thruster import Thruster
from environment.forces import drag_force, solar_pressure_force
from environment.gravity import gravity_force
from environment.space import Space
from physics.body import Body
from physics.dynamics import add_forces, compute_acceleration
from physics.integrator import euler_step
from utils.utils import distance


class Simulator:
    def __init__(self, config, ga, astar):
        self.config = config
        self.ga = ga
        self.astar = astar
        self.body = Body(list(config.START), list(config.INITIAL_VELOCITY), config.MASS, config.FUEL)
        self.space = Space(config.SPACE_WIDTH, config.SPACE_HEIGHT, config.TARGET, config.CAPTURE_RADIUS, config.CAPTURE_SPEED)
        self.thruster = Thruster()
        self.route = []
        self.status = "not started"

    def plan_route(self):
        start_state = self.body.state()
        waypoint = self.ga.evolve(start_state, self.config.TARGET)
        first_leg = self.astar.plan(start_state, waypoint)
        second_leg = self.astar.plan(waypoint, self.config.TARGET)
        self.route = self.smooth_path(first_leg + second_leg[1:])
        return waypoint, self.route

    def run(self, verbose=True):
        trajectory = [(self.body.position[0], self.body.position[1])]
        waypoint, route = self.plan_route()
        route_index = 0
        if verbose:
            print(f"Start: ({self.config.START[0]:.2f}, {self.config.START[1]:.2f})")
            print(f"Target: ({self.config.TARGET[0]:.2f}, {self.config.TARGET[1]:.2f})")
            print(f"GA waypoint: ({waypoint[0]:.2f}, {waypoint[1]:.2f})")
            print(f"A* route length: {len(route)} points")
        for _ in range(1, self.config.STEPS + 1):
            target_index = min(route_index + self.config.LOOKAHEAD, len(route) - 1)
            if distance(self.body.position, route[target_index]) <= self.config.WAYPOINT_RADIUS:
                route_index = target_index
                target_index = min(route_index + self.config.LOOKAHEAD, len(route) - 1)
            thrust = self.thruster.command(route[target_index], self.body, self.config.DT)
            gravity = gravity_force(self.body.position, self.config.GRAVITY_SOURCE, self.config.GRAVITATIONAL_PARAMETER, self.body.mass)
            drag = drag_force(self.body.velocity, self.config.DRAG_COEFFICIENT)
            solar = solar_pressure_force(magnitude_value=self.config.SOLAR_PRESSURE)
            acceleration = compute_acceleration(self.body, add_forces(thrust, gravity, drag, solar))
            euler_step(self.body, acceleration, self.config.DT)
            trajectory.append((self.body.position[0], self.body.position[1]))
            if self.space.captured(self.body.position, self.body.velocity):
                self.status = "captured"
                break
            if not self.space.in_bounds(self.body.position):
                self.status = "out of bounds"
                break
            if distance(self.body.position, self.config.START) > self.config.MAX_DISTANCE:
                self.status = "maximum distance exceeded"
                break
            if self.body.fuel <= 0:
                self.status = "fuel exhausted"
                break
        else:
            self.status = "step limit reached"
        if verbose:
            print(f"Status: {self.status}")
            print(f"Steps: {len(trajectory) - 1} | Fuel used: {self.body.fuel_used:.2f} | Fuel remaining: {self.body.fuel:.2f}")
            print(f"Final position: ({self.body.position[0]:.2f}, {self.body.position[1]:.2f})")
            print(f"Final speed: {math.hypot(*self.body.velocity):.2f}")
        return trajectory

    @staticmethod
    def smooth_path(path):
        if len(path) < 3:
            return list(path)
        smoothed = [path[0]]
        for previous, current, following in zip(path, path[1:], path[2:]):
            smoothed.append(((previous[0] + 2 * current[0] + following[0]) / 4, (previous[1] + 2 * current[1] + following[1]) / 4))
        smoothed.append(path[-1])
        return smoothed

    def plot(self, trajectory, show=True, output_path=None):
        if not trajectory:
            raise ValueError("trajectory cannot be empty")
        xs, ys = zip(*trajectory)
        figure, axis = plt.subplots()
        axis.plot(xs, ys, linewidth=2, label="Simulated trajectory")
        if self.route:
            route_xs, route_ys = zip(*self.route)
            axis.plot(route_xs, route_ys, "--", alpha=0.7, label="Planned route")
        axis.scatter(*self.config.START, c="green", s=80, label="Start")
        axis.scatter(*self.config.TARGET, c="red", s=100, label="Target")
        axis.scatter(*self.config.GRAVITY_SOURCE, c="black", s=50, label="Gravity source")
        axis.set(xlabel="X position", ylabel="Y position", title=f"Satellite trajectory ({self.status})")
        axis.set_aspect("equal", adjustable="box")
        axis.set_xlim(0, self.config.SPACE_WIDTH)
        axis.set_ylim(0, self.config.SPACE_HEIGHT)
        axis.grid(True)
        axis.legend()
        if output_path:
            figure.savefig(output_path, dpi=150, bbox_inches="tight")
        if show:
            plt.show()
        else:
            plt.close(figure)
