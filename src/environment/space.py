import math

class Space:
    def __init__(self, width, height, target, capture_radius=2.0, deadzone_radius=0.5):
        self.width = width
        self.height = height
        self.target = target
        self.capture_radius = capture_radius
        self.deadzone_radius = deadzone_radius

    def in_bounds(self, pos):
        x, y = pos
        return 0 <= x <= self.width and 0 <= y <= self.height

    def in_deadzone(self, pos):
        dx = pos[0] - self.target[0]
        dy = pos[1] - self.target[1]
        return math.hypot(dx, dy) < self.deadzone_radius

    def captured(self, pos, velocity):
        dx = pos[0] - self.target[0]
        dy = pos[1] - self.target[1]
        dist = math.hypot(dx, dy)
        speed = math.hypot(velocity[0], velocity[1])
        return dist < self.capture_radius and speed < 0.5
