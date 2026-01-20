Satellite-Trajectory-AI/
│
├── .gitignore
├── README.md
├── requirements.txt
│
├── docs/
│   ├── problem_statement.md
│   ├── physics_model.md
│   ├── algorithms.md
│   ├── results.md
│
├── src/
│   ├── main.py
│   │
│   ├── environment/
│   │   ├── __init__.py
│   │   ├── space.py          # world, boundaries
│   │   ├── gravity.py        # gravity fields
│   │   ├── forces.py         # drag, solar pressure
│   │
│   ├── physics/
│   │   ├── __init__.py
│   │   ├── body.py           # satellite state
│   │   ├── integrator.py     # Euler / Verlet
│   │   ├── dynamics.py       # motion equations
│   │
│   ├── control/
│   │   ├── __init__.py
│   │   ├── thruster.py
│   │   ├── attitude.py       # optional
│   │
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── astar.py
│   │   ├── genetic.py
│   │   ├── fitness.py
│   │
│   ├── simulation/
│   │   ├── __init__.py
│   │   ├── simulator.py
│   │   ├── config.py
│   │
│   └── utils/
│       ├── logger.py
│       ├── constants.py
│
├── experiments/
│   ├── astar_test.py
│   ├── ga_test.py
│
├── results/
│   ├── plots/
│   ├── trajectories/
│
└── tests/
    ├── test_physics.py
    ├── test_gravity.py
