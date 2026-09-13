from utils.utils import distance, magnitude


class Space:
    def __init__(self, width, height, target, capture_radius=8.0, capture_speed=1.5):
        if width <= 0 or height <= 0:
            raise ValueError("space dimensions must be positive")
        self.width = float(width)
        self.height = float(height)
        self.target = (float(target[0]), float(target[1]))
        self.capture_radius = float(capture_radius)
        self.capture_speed = float(capture_speed)

    def in_bounds(self, position):
        return 0.0 <= position[0] <= self.width and 0.0 <= position[1] <= self.height

    def in_deadzone(self, position):
        return distance(position, self.target) < self.capture_radius

    def captured(self, position, velocity):
        return self.in_deadzone(position) and magnitude(velocity) <= self.capture_speed
