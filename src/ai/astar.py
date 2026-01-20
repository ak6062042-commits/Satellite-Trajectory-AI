import math

class AStarPlanner:
    def plan(self, state, goal, gravity_fn, dt=0.05):
        sx, sy, vx, vy = state
        gx, gy = goal

        actions = [
            (0,0), (1,0), (-1,0), (0,1), (0,-1),
            (1,1), (-1,-1), (1,-1), (-1,1)
        ]

        best_cost = float("inf")
        best_target = (sx, sy)

        for ax, ay in actions:
            px, py = sx, sy
            pvx, pvy = vx, vy
            cost = 0.0

            for _ in range(10):
                gx_f, gy_f = gravity_fn((px, py))
                pvx += (ax + gx_f) * dt
                pvy += (ay + gy_f) * dt
                px += pvx * dt
                py += pvy * dt

                d = math.hypot(px - gx, py - gy)
                v = math.hypot(pvx, pvy)
                gravity_alignment = (pvx * gx_f + pvy * gy_f)
                cost += d + 0.2 * v - 0.05 * gravity_alignment


            if cost < best_cost:
                best_cost = cost
                best_target = (px, py)

        return best_target
