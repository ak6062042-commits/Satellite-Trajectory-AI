# Satellite Trajectory AI

A runnable two-dimensional satellite-transfer simulator that combines a genetic waypoint search, bounded A* routing, and force-based trajectory following.

The project is an educational planning and controls sandbox. It does not attempt to be a high-fidelity orbital mechanics package.

## What it does

- Models a satellite with position, velocity, mass, and finite fuel.
- Plans an intermediate waypoint with a seeded genetic algorithm.
- Builds a bounded, eight-direction A* route through the workspace.
- Applies thrust, softened point-mass gravity, optional quadratic drag, and optional solar pressure.
- Stops on target capture, fuel exhaustion, boundary exit, excessive drift, or a step limit.
- Produces an optional plot of both planned and simulated trajectories.

## Quick start

Use Python 3.10 or newer.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python src/main.py
```

The default deterministic scenario starts at `(60, 75)` and targets `(340, 315)`. With seed `7`, it captures the target in 820 steps.

## Command-line options

```powershell
python src/main.py --seed 12
python src/main.py --plot
python src/main.py --save-plot trajectory.png
```

`--seed` controls the genetic planner's random source. `--plot` opens an interactive chart; `--save-plot` writes the chart without opening a window.

## Configuration

Edit `src/simulation/config.py` to define another mission. The `Config` dataclass exposes workspace dimensions, initial state, target, integration time step, fuel, capture conditions, planning grid size, environmental forces, and random seed.

To use the components directly, add `src` to Python's import path and compose a configuration, planners, and simulator:

```python
from ai.astar import AStarPlanner
from ai.genetic import GeneticPlanner
from simulation.config import Config
from simulation.simulator import Simulator

config = Config()
simulator = Simulator(
    config,
    GeneticPlanner(config),
    AStarPlanner(config.SPACE_WIDTH, config.SPACE_HEIGHT, config.GRID_RESOLUTION),
)
trajectory = simulator.run()
```

## Project layout

```text
src/
  ai/           waypoint fitness, genetic search, and A* planning
  control/      thrust and heading utilities
  environment/  workspace and external force models
  physics/      body state, force aggregation, and integration
  simulation/   mission configuration and execution
  main.py       command-line entry point
docs/
  problem_statement.md
  physics_model.md
  algorithms.md
  results.md
```

## Documentation

- [Problem statement](docs/problem_statement.md)
- [Physics model](docs/physics_model.md)
- [Algorithms](docs/algorithms.md)
- [Results and reproducibility](docs/results.md)

## Limitations

This is a planar point-mass simulation. It excludes true orbital elements, three-dimensional motion, real propulsion models, rotating reference frames, and obstacle generation. Treat its output as an algorithmic demonstration, not a navigational or mission-design result.
