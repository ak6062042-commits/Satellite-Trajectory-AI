import random
from ai.fitness import evaluate_waypoint

class GeneticPlanner:
    def __init__(self, config):
        self.config = config

    def evolve(self, start):
        population = [
            (
                random.uniform(0, self.config.SPACE_WIDTH),
                random.uniform(0, self.config.SPACE_HEIGHT)
            )
            for _ in range(30)
        ]
        for _ in range(20):
            scored = [(evaluate_waypoint(start, wp), wp) for wp in population]
            scored.sort(key=lambda x: x[0])
            population = [wp for _, wp in scored[:15]]
            while len(population) < 30:
                x, y = random.choice(population)
                population.append((
                    x + random.uniform(-30, 30),
                    y + random.uniform(-30, 30)
                ))
        return population[0]
