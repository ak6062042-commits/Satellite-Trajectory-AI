import math


class Attitude:
    def __init__(self, angle=0.0, max_turn_rate=math.pi):
        self.angle = float(angle)
        self.max_turn_rate = float(max_turn_rate)

    def aim_at(self, source, target, dt):
        desired = math.atan2(target[1] - source[1], target[0] - source[0])
        delta = (desired - self.angle + math.pi) % (2 * math.pi) - math.pi
        limit = self.max_turn_rate * dt
        self.angle += max(-limit, min(limit, delta))
        return self.angle

    def direction(self):
        return (math.cos(self.angle), math.sin(self.angle))
