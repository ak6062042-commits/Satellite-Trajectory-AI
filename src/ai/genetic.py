import random

from ai.fitness import evaluate_waypoint
from utils.utils import clamp


class GeneticPlanner:
    def __init__(self, config, population_size=40, generations=30, seed=None):
        self.config = config
        self.population_size = int(population_size)
        self.generations = int(generations)
        self.random = random.Random(seed if seed is not None else config.RANDOM_SEED)

    def evolve(self, start, goal=None):
        goal = goal or self.config.TARGET
        midpoint = ((start[0] + goal[0]) / 2, (start[1] + goal[1]) / 2)
        spread = max(self.config.SPACE_WIDTH, self.config.SPACE_HEIGHT) * 0.2
        population = [
            (
                clamp(midpoint[0] + self.random.uniform(-spread, spread), 0.0, self.config.SPACE_WIDTH),
                clamp(midpoint[1] + self.random.uniform(-spread, spread), 0.0, self.config.SPACE_HEIGHT),
            )
            for _ in range(self.population_size)
        ]
        population[0] = midpoint
        elite_size = max(2, self.population_size // 4)
        for generation in range(self.generations):
            scored = sorted(
                (
                    evaluate_waypoint(start, waypoint, goal, self.config.SPACE_WIDTH, self.config.SPACE_HEIGHT),
                    waypoint,
                )
                for waypoint in population
            )
            elites = [waypoint for _, waypoint in scored[:elite_size]]
            mutation = spread * (1.0 - generation / self.generations) * 0.35
            population = elites.copy()
            while len(population) < self.population_size:
                first = self.random.choice(elites)
                second = self.random.choice(elites)
                population.append(
                    (
                        clamp((first[0] + second[0]) / 2 + self.random.uniform(-mutation, mutation), 0.0, self.config.SPACE_WIDTH),
                        clamp((first[1] + second[1]) / 2 + self.random.uniform(-mutation, mutation), 0.0, self.config.SPACE_HEIGHT),
                    )
                )
        return min(
            population,
            key=lambda waypoint: evaluate_waypoint(start, waypoint, goal, self.config.SPACE_WIDTH, self.config.SPACE_HEIGHT),
        )
