import random

class Config:
    SPACE_WIDTH = 500
    SPACE_HEIGHT = 500

    START = (random.uniform(0, SPACE_WIDTH), random.uniform(0, SPACE_HEIGHT))
    TARGET = (random.uniform(0, SPACE_WIDTH), random.uniform(0, SPACE_HEIGHT))

    INITIAL_VELOCITY = (0.0, 0.0)
    DT = 0.05
    STEPS = 3000

    CAPTURE_RADIUS = 1.0
    CAPTURE_SPEED = 0.5
    MAX_DISTANCE = 1000.0
    LOOKAHEAD = 3  # how many nodes ahead to target
