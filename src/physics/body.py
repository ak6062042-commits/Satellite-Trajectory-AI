from dataclasses import dataclass, field

from utils.constants import DEFAULT_FUEL, DEFAULT_SATELLITE_MASS


@dataclass
class Body:
    position: list[float]
    velocity: list[float]
    mass: float = DEFAULT_SATELLITE_MASS
    fuel: float = DEFAULT_FUEL
    initial_fuel: float = field(init=False)

    def __post_init__(self):
        self.position = [float(self.position[0]), float(self.position[1])]
        self.velocity = [float(self.velocity[0]), float(self.velocity[1])]
        self.mass = float(self.mass)
        self.fuel = float(self.fuel)
        if self.mass <= 0:
            raise ValueError("mass must be positive")
        if self.fuel < 0:
            raise ValueError("fuel cannot be negative")
        self.initial_fuel = self.fuel

    @property
    def fuel_used(self):
        return self.initial_fuel - self.fuel

    def burn_fuel(self, amount):
        amount = max(0.0, float(amount))
        consumed = min(self.fuel, amount)
        self.fuel -= consumed
        return consumed

    def state(self):
        return (self.position[0], self.position[1], self.velocity[0], self.velocity[1])
