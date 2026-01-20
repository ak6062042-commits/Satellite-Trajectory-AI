import random

class Config:
    SPACE_WIDTH = 400
    SPACE_HEIGHT = 400

    START = (random.uniform(50, 350), random.uniform(50, 350))
    TARGET = (random.uniform(50, 350), random.uniform(50, 350))

    INITIAL_VELOCITY = (0.0, 0.0)
    DT = 0.05
    STEPS = 4000
