# Algorithms

## Genetic waypoint selection

`GeneticPlanner` searches for one waypoint between the initial state and target. It seeds a population around the midpoint, ranks candidates by route length and current speed, retains an elite set, and generates the next population through crossover and bounded mutation.

The waypoint objective is:

```text
distance(start, waypoint) + distance(waypoint, target) + 0.1 * initial_speed
```

Candidates outside the workspace receive a large penalty. A configurable random seed makes results reproducible.

## A* route planning

`AStarPlanner` converts continuous positions to nodes on a finite grid. It uses eight connected moves, Euclidean step costs, and Euclidean heuristic distance. Since the heuristic is admissible for this movement model, A* returns a shortest grid route when a route exists.

The planner accepts optional blocked grid nodes and rejects blocked start or goal nodes. It always preserves the original continuous start and goal as the first and last points in the returned path.

## Route following

The simulator lightly smooths interior grid nodes with a three-point weighted average. The controller aims several points ahead, advances its route target once that target falls inside the waypoint radius, and commands bounded thrust to close the velocity error. This gives the craft room to brake near the target rather than blindly applying maximum force.

## Complexity

For a grid with `V` reachable nodes and `E` edges, A* runs in `O((V + E) log V)` time and uses `O(V)` memory. The genetic stage runs in `O(population_size * generations)` objective evaluations. The simulation is linear in the number of integration steps actually executed.
