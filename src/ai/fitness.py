import math

def evaluate_waypoint(state, waypoint, gravity_fn):
    sx, sy, vx, vy = state
    wx, wy = waypoint

    d = math.hypot(wx - sx, wy - sy)
    v = math.hypot(vx, vy)

    gx, gy = gravity_fn((sx, sy))
    align = abs((gx*(wx-sx) + gy*(wy-sy)) / (d + 1e-6))

    return d + 0.4*v - 2.0*align
