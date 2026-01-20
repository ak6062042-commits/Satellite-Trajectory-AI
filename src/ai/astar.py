import heapq
import math

class AStarPlanner:
    def plan(self, start, goal):
        sx, sy, _, _ = start
        gx, gy = goal
        start = (round(sx), round(sy))
        goal = (round(gx), round(gy))
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        moves = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
        while open_set:
            _, current = heapq.heappop(open_set)
            if current == goal:
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                return path[::-1]
            for dx, dy in moves:
                nxt = (current[0] + dx, current[1] + dy)
                cost = g_score[current] + math.hypot(dx, dy)
                if nxt not in g_score or cost < g_score[nxt]:
                    g_score[nxt] = cost
                    h = math.hypot(nxt[0] - goal[0], nxt[1] - goal[1])
                    heapq.heappush(open_set, (cost + h, nxt))
                    came_from[nxt] = current
        return [start]
