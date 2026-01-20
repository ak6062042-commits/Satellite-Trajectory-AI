import math

def evaluate_waypoint(start, waypoint):
    sx, sy, vx, vy = start
    wx, wy = waypoint
    d = math.hypot(wx - sx, wy - sy)
    v = math.hypot(vx, vy)
    return d + 0.3 * v
