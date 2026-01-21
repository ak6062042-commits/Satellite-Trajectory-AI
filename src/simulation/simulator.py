# simulation/simulator.py
from ai.astar import AStarPlanner
from ai.genetic import GAPlanner
from physics.body import Body
from simulation.config import MAX_FUEL

class Simulator:
    def __init__(self, start, target):
        self.body = Body(*start, fuel=MAX_FUEL)
        self.target = target

    def run(self):
        ga = GAPlanner(
            (self.body.x, self.body.y, self.body.vx, self.body.vy),
            self.target
        )
        waypoint = ga.run()

        astar = AStarPlanner()
        came, end = astar.plan(
            (self.body.x, self.body.y, self.body.vx, self.body.vy),
            waypoint
        )

        if not end:
            print("A* failed")
            return []

        return self.body.path
