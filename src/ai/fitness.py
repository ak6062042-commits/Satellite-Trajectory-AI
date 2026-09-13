from utils.utils import distance, magnitude


def evaluate_waypoint(start, waypoint, goal, width=None, height=None):
    start_position = (start[0], start[1])
    score = distance(start_position, waypoint) + distance(waypoint, goal)
    score += 0.1 * magnitude((start[2], start[3]))
    if width is not None and not 0.0 <= waypoint[0] <= width:
        score += 1_000_000.0
    if height is not None and not 0.0 <= waypoint[1] <= height:
        score += 1_000_000.0
    return score
