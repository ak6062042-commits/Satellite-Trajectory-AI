import math

def evaluate_waypoint(state, waypoint):
    x, y, vx, vy = state
    wx, wy = waypoint

    dx = wx - x
    dy = wy - y
    dist = math.hypot(dx, dy)

    kinetic = 0.5 * (vx*vx + vy*vy)

    return dist + 0.4 * kinetic
