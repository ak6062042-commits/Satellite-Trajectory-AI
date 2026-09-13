from math import hypot


def clamp(value, lower, upper):
    return max(lower, min(value, upper))


def distance(first, second):
    return hypot(first[0] - second[0], first[1] - second[1])


def magnitude(vector):
    return hypot(vector[0], vector[1])


def log(message):
    print(message)
