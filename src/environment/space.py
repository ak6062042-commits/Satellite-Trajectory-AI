import math

class Space:
    def __init__(self, target):
        self.target = target

    def captured(self, pos, vel):
        d = math.hypot(pos[0]-self.target[0], pos[1]-self.target[1])
        v = math.hypot(vel[0], vel[1])
        return d < 5 and v < 3
