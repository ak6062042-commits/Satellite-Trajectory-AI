from simulation.config import Config
from simulation.simulator import Simulator
from ai.genetic import GeneticPlanner
from ai.astar import AStarPlanner

def main():
    config = Config()
    ga = GeneticPlanner(config)
    astar = AStarPlanner()
    sim = Simulator(config, ga, astar)
    trajectory = sim.run()
    sim.plot(trajectory)

if __name__ == "__main__":
    main()
