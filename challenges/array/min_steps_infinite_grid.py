

def cover_points(points):
    """
    Find the minimum number of steps to cover a sequence of points in the
    order they need to be covered.
    The points are in an infinite 2D grid and one can move in any of the
    8 directions.

        points = [(0,0, (2,2), (0,5)]

          0 1 2
        0 *
        1   \
        2     *
        3   /
        4 |
        5 *
    """
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
