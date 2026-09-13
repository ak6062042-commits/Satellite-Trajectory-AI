import argparse

from ai.astar import AStarPlanner
from ai.genetic import GeneticPlanner
from simulation.config import Config
from simulation.simulator import Simulator


def build_parser():
    parser = argparse.ArgumentParser(description="Plan and simulate a 2D satellite trajectory.")
    parser.add_argument("--seed", type=int, default=7, help="Random seed used by the genetic planner.")
    parser.add_argument("--plot", action="store_true", help="Display a trajectory plot after the simulation.")
    parser.add_argument("--save-plot", metavar="PATH", help="Save the trajectory plot to PATH.")
    return parser


def main():
    arguments = build_parser().parse_args()
    config = Config(RANDOM_SEED=arguments.seed)
    ga = GeneticPlanner(config)
    astar = AStarPlanner(config.SPACE_WIDTH, config.SPACE_HEIGHT, config.GRID_RESOLUTION)
    simulator = Simulator(config, ga, astar)
    trajectory = simulator.run()
    if arguments.plot or arguments.save_plot:
        simulator.plot(trajectory, show=arguments.plot, output_path=arguments.save_plot)


if __name__ == "__main__":
    main()
