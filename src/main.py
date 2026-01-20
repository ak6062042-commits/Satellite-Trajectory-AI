from simulation.config import Config
from simulation.simulator import Simulator
from ai.genetic import GeneticPlanner
from ai.astar import AStarPlanner
from environment.gravity import gravity_force

def main():
    config = Config()
    ga = GeneticPlanner(config, gravity_force)
    astar = AStarPlanner()
    sim = Simulator(config, ga, astar)
    traj = sim.run()
    sim.plot(traj)

if __name__ == "__main__":
    main()
