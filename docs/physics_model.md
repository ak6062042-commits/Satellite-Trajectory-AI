# Physics model

The project uses a discrete two-dimensional point-mass model. It is intended for algorithm experimentation and visualization, not high-fidelity astrodynamics.

At each time step, the net force is

```text
F_net = F_thrust + F_gravity + F_drag + F_solar
```

Acceleration follows Newton's second law:

```text
a = F_net / m
```

The semi-implicit Euler update advances velocity before position:

```text
v(t + dt) = v(t) + a(t) dt
x(t + dt) = x(t) + v(t + dt) dt
```

## Forces

`gravity_force` applies a softened point-mass attraction toward `GRAVITY_SOURCE`:

```text
F_gravity = m mu r / (|r|^2 + epsilon^2)^(3/2)
```

Softening prevents a singularity at the gravity source. The thruster is a bounded velocity-feedback controller: it determines a desired velocity toward the current route point, limits the commanded force, and burns fuel from that command. Drag is quadratic in speed and can be disabled by setting `DRAG_COEFFICIENT` to zero. Solar pressure is modeled as an optional constant directional force and defaults to zero.

## Scope and limitations

There are no three-dimensional orbital elements, rotating frames, collision geometry, attitude coupling, or real propulsion curves. The `Attitude` utility tracks a turn-limited heading, but the baseline simulator uses direct translational thrust. These simplifications keep planning behavior inspectable and repeatable.
