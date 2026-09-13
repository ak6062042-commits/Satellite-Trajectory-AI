# Results

## Reproducible baseline

Run the default scenario from the repository root:

```powershell
python src/main.py
```

With the bundled defaults and seed `7`, the run reports a captured target after 820 integration steps. The final position is approximately `(339.82, 314.95)`, final speed is approximately `1.47`, and fuel remaining is approximately `292.23`.

These values are a regression baseline rather than a scientific benchmark. They may change when the physics constants, Python version, or planner parameters change.

## Plot output

To save a plot without opening a window:

```powershell
python src/main.py --save-plot trajectory.png
```

The plot shows the simulated path, planned route, start, target, and gravity source. Use `--plot` to display it interactively.

## Interpreting outcomes

`captured` indicates the position and speed capture conditions were both satisfied. Other terminal states are diagnostic: `fuel exhausted`, `out of bounds`, `maximum distance exceeded`, and `step limit reached` indicate which constraint halted a run. For fair comparisons, keep the random seed fixed and change one configuration value at a time.
