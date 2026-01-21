# planners/astar.py
import heapq
import math
from simulation.config import GRID_POS, GRID_V, MAX_THRUST
from environment.gravity import gravity_accel

class AStarPlanner:
    def __init__(self):
        pass

    def plan(self, start, goal):
        sx, sy, svx, svy = start
        gx, gy = goal

        def h(x, y, vx, vy):
            return math.hypot(gx - x, gy - y) / (math.hypot(vx, vy) + 1.0)

        open_set = []
        heapq.heappush(open_set, (0, (sx, sy, svx, svy)))
        came = {}
        cost = { (sx, sy, svx, svy): 0 }

        while open_set:
            _, (x, y, vx, vy) = heapq.heappop(open_set)

            if math.hypot(x - gx, y - gy) < GRID_POS:
                return came, (x, y, vx, vy)

            for ax, ay in self._actions():
                gx_acc, gy_acc = gravity_accel(x, y)

                nvx = vx + (ax + gx_acc)
                nvy = vy + (ay + gy_acc)
                nx = x + nvx
                ny = y + nvy

                node = (
                    round(nx / GRID_POS) * GRID_POS,
                    round(ny / GRID_POS) * GRID_POS,
                    round(nvx / GRID_V) * GRID_V,
                    round(nvy / GRID_V) * GRID_V
                )

                new_cost = cost[(x,y,vx,vy)] + (ax*ax + ay*ay)

                if node not in cost or new_cost < cost[node]:
                    cost[node] = new_cost
                    priority = new_cost + h(*node)
                    heapq.heappush(open_set, (priority, node))
                    came[node] = (x,y,vx,vy)

        return None, None

    def _actions(self):
        return [
            (0,0),                                  # COAST
            ( MAX_THRUST, 0),
            (-MAX_THRUST, 0),
            (0,  MAX_THRUST),
            (0, -MAX_THRUST)
        ]
