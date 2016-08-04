"""
You are in an infinite 2D grid where you can move in any of the 8 directions.
You are given a sequence of points and the order in which you need to cover
the points. Give the minimum number of steps in which you can achieve it.
You start from the first point.
"""


def cover_points(points):
    moves = 0
    for prev_point, point in zip(points, points[1:]):
        prev_x, prev_y = prev_point
        x, y = point

        x_dist = abs(x - prev_x)
        y_dist = abs(y - prev_y)
        moves += max(x_dist, y_dist)

    return moves


def test_min_steps_cover_points():
    assert cover_points([(0, 0), (-2, 2)]) == 2
    assert cover_points([(0, 0), (-4, 2), (0, -2)]) == 8
    assert cover_points([(0, 0), (1, 1), (5, 2)]) == 5
