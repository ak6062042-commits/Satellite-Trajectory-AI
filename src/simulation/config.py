# config.py

DT = 0.1
MAX_STEPS = 4000

# Spacecraft
MAX_THRUST = 40.0
MAX_FUEL = 10000.0
FUEL_COST_PER_THRUST = 0.02
MASS = 1.0

# Gravity body (planet)
GRAVITY_MU = 5000.0
PLANET_POS = (0.0, 0.0)

# A*
GRID_V = 2.0          # velocity discretization
GRID_POS = 5.0        # position discretization
ASTAR_MAX_NODES = 30000

# GA
GA_POP = 40
GA_GEN = 40
