# main.py
from simulation.simulator import Simulator
from utils.utils import plot

def main():
    start = (-250, -250, 0.0, 2.5)
    target = (200, 150)

    sim = Simulator(start, target)
    path = sim.run()

    plot(path, target)

if __name__ == "__main__":
    main()
