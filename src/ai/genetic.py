# planners/ga.py
import random
import math
from simulation.config import GA_POP, GA_GEN

class GAPlanner:
    def __init__(self, start, target):
        self.start = start
        self.target = target

    def run(self):
        pop = [self.random_wp() for _ in range(GA_POP)]

        for _ in range(GA_GEN):
            scored = [(self.fitness(wp), wp) for wp in pop]
            scored.sort(key=lambda x: x[0])
            pop = [wp for _, wp in scored[:GA_POP//2]]
            pop += [self.mutate(random.choice(pop)) for _ in range(GA_POP//2)]

        return min(pop, key=self.fitness)

    def fitness(self, wp):
        sx, sy, _, _ = self.start
        wx, wy = wp
        tx, ty = self.target

        d1 = math.hypot(wx - sx, wy - sy)
        d2 = math.hypot(tx - wx, ty - wy)

        angle = abs(math.atan2(wy, wx))
        return d1 + d2 - 200 * math.sin(angle)

    def random_wp(self):
        return (
            random.uniform(-300, 300),
            random.uniform(-300, 300)
        )

    def mutate(self, wp):
        return (
            wp[0] + random.uniform(-20,20),
            wp[1] + random.uniform(-20,20)
        )
