from dataclasses import dataclass

from utils.constants import DEFAULT_MAX_STEPS, DEFAULT_SPACE_HEIGHT, DEFAULT_SPACE_WIDTH, DEFAULT_TIME_STEP


@dataclass
class Config:
    SPACE_WIDTH: float = DEFAULT_SPACE_WIDTH
    SPACE_HEIGHT: float = DEFAULT_SPACE_HEIGHT
    START: tuple[float, float] = (60.0, 75.0)
    TARGET: tuple[float, float] = (340.0, 315.0)
    INITIAL_VELOCITY: tuple[float, float] = (0.0, 0.0)
    DT: float = DEFAULT_TIME_STEP
    STEPS: int = DEFAULT_MAX_STEPS
    MASS: float = 1.0
    FUEL: float = 300.0
    CAPTURE_RADIUS: float = 8.0
    CAPTURE_SPEED: float = 1.5
    MAX_DISTANCE: float = 650.0
    LOOKAHEAD: int = 3
    WAYPOINT_RADIUS: float = 6.0
    GRID_RESOLUTION: float = 10.0
    GRAVITY_SOURCE: tuple[float, float] = (200.0, 450.0)
    GRAVITATIONAL_PARAMETER: float = 600.0
    DRAG_COEFFICIENT: float = 0.001
    SOLAR_PRESSURE: float = 0.0
    RANDOM_SEED: int | None = 7

    def __post_init__(self):
        if self.SPACE_WIDTH <= 0 or self.SPACE_HEIGHT <= 0:
            raise ValueError("space dimensions must be positive")
        if self.DT <= 0 or self.STEPS <= 0:
            raise ValueError("DT and STEPS must be positive")
        if self.MASS <= 0 or self.FUEL < 0:
            raise ValueError("MASS must be positive and FUEL cannot be negative")
        for point in (self.START, self.TARGET, self.GRAVITY_SOURCE):
            if len(point) != 2:
                raise ValueError("points must contain two coordinates")
