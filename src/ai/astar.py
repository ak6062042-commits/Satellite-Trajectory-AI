import heapq
import math


class AStarPlanner:
    def __init__(self, width=400.0, height=400.0, resolution=10.0, blocked=None):
        if width <= 0 or height <= 0 or resolution <= 0:
            raise ValueError("width, height, and resolution must be positive")
        self.width = float(width)
        self.height = float(height)
        self.resolution = float(resolution)
        self.columns = math.ceil(self.width / self.resolution)
        self.rows = math.ceil(self.height / self.resolution)
        self.blocked = set(blocked or ())

    def plan(self, start, goal):
        start_point = (float(start[0]), float(start[1]))
        goal_point = (float(goal[0]), float(goal[1]))
        start_node = self._to_node(start_point)
        goal_node = self._to_node(goal_point)
        if start_node in self.blocked or goal_node in self.blocked:
            raise ValueError("start and goal must not be blocked")
        frontier = [(0.0, 0.0, start_node)]
        predecessors = {}
        costs = {start_node: 0.0}
        while frontier:
            _, current_cost, current = heapq.heappop(frontier)
            if current_cost != costs[current]:
                continue
            if current == goal_node:
                nodes = self._reconstruct(predecessors, current)
                points = [self._to_point(node) for node in nodes]
                points[0] = start_point
                points[-1] = goal_point
                return points
            for neighbor, step_cost in self._neighbors(current):
                if neighbor in self.blocked:
                    continue
                cost = current_cost + step_cost
                if cost < costs.get(neighbor, math.inf):
                    costs[neighbor] = cost
                    predecessors[neighbor] = current
                    heuristic = math.hypot(neighbor[0] - goal_node[0], neighbor[1] - goal_node[1])
                    heapq.heappush(frontier, (cost + heuristic, cost, neighbor))
        raise RuntimeError("no route found")

    def _to_node(self, point):
        x = min(max(point[0], 0.0), self.width)
        y = min(max(point[1], 0.0), self.height)
        return (min(self.columns, round(x / self.resolution)), min(self.rows, round(y / self.resolution)))

    def _to_point(self, node):
        return (min(node[0] * self.resolution, self.width), min(node[1] * self.resolution, self.height))

    def _neighbors(self, node):
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            neighbor = (node[0] + dx, node[1] + dy)
            if 0 <= neighbor[0] <= self.columns and 0 <= neighbor[1] <= self.rows:
                yield neighbor, math.hypot(dx, dy)

    @staticmethod
    def _reconstruct(predecessors, current):
        path = [current]
        while current in predecessors:
            current = predecessors[current]
            path.append(current)
        return list(reversed(path))
