# Problem statement

This project models a planar satellite-transfer problem in a bounded two-dimensional workspace. A satellite starts with a position, velocity, mass, and finite fuel supply. It must reach a target region with a sufficiently low speed while remaining within the simulation boundary.

The simulation combines route planning with force-based motion. A genetic planner chooses an intermediate waypoint, A* turns the two legs into a bounded grid route, and a feedback thruster follows that route while accounting for gravity and drag.

## Mission constraints

- The world is a rectangle from `(0, 0)` to `(SPACE_WIDTH, SPACE_HEIGHT)`.
- A mission succeeds only when the satellite is inside the capture radius and below the capture-speed limit.
- Fuel is consumed in proportion to commanded thrust.
- The run ends on capture, fuel exhaustion, an out-of-bounds state, excessive drift, or the configured step limit.

## Default scenario

The default configuration transfers a stationary satellite from `(60, 75)` to `(340, 315)` in a `400 x 400` workspace. A gravity source at `(200, 450)` creates a small perturbation without sitting on the nominal transit corridor. Values are deliberately exposed through `simulation/config.py` so that scenarios can be changed without altering algorithms.
