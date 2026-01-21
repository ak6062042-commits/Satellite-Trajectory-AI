# utils/plotter.py
import matplotlib.pyplot as plt
from simulation.config import PLANET_POS

def plot(path, target):
    xs = [p[0] for p in path]
    ys = [p[1] for p in path]

    plt.plot(xs, ys)
    plt.scatter(*PLANET_POS)
    plt.scatter(*target)
    plt.axis("equal")
    plt.grid()
    plt.show()
