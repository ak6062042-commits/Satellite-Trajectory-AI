import random
from ai.fitness import evaluate_waypoint

class GeneticPlanner:
    def __init__(self, config, gravity_fn):
        self.config = config
        self.gravity_fn = gravity_fn

    def evolve(self, state):
        population = [
            (
                random.uniform(0, self.config.SPACE_WIDTH),
                random.uniform(0, self.config.SPACE_HEIGHT)
            )
            for _ in range(40)
        ]

        for _ in range(25):
            scored = [(evaluate_waypoint(state, wp, self.gravity_fn), wp) for wp in population]
            scored.sort(key=lambda x: x[0])
            elite = [wp for _, wp in scored[:15]]

            population = elite[:]
            while len(population) < 40:
                x, y = random.choice(elite)
                population.append((
                    x + random.uniform(-40, 40),
                    y + random.uniform(-40, 40)
                ))

        return population[0]
