import sys
import collections


def calculate_slope(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    if x2 - x1 == 0:
        return sys.maxint
    else:
        return float(y2 - y1) / float(x2 - x1)


def max_points_on_straight_line(points):
    if len(points) < 2:
        return len(points)

    unique_points = collections.Counter(points)
    points = unique_points.keys()
    slopes = collections.defaultdict(collections.Counter)

    for idx, point in enumerate(points):
        for other_point in points[idx+1:]:
            slope = calculate_slope(point, other_point)
            print(point, other_point, slope)

            other_point_count = unique_points[other_point]
            slopes[point][slope] += other_point_count
            slopes[other_point][slope] += other_point_count

    max_points = 0
    for p, count in unique_points.items():
        counter = slopes[p]

        print(p, counter)

        try:
            _, most_common_count = counter.most_common(1)[0]
        except IndexError:
            most_common_count = 0

        max_points = max(max_points, most_common_count + count)

    return max_points


def test_minus_points():
    assert max_points_on_straight_line([(0, 0), (1, 1), (-1, -1)]) == 3


def test_max_points():
    assert max_points_on_straight_line([]) == 0
    assert max_points_on_straight_line([(1, 1)]) == 1
    assert max_points_on_straight_line([(1, 1), (3, 3)]) == 2
    assert max_points_on_straight_line([(1, 0), (2, 0), (3, 0), (3, 3), (3, 4)]) == 3


def test_zero_division():
    assert max_points_on_straight_line([(1, 0), (2, 0), (3, 0)]) == 3


def test_same_x_axis():
    assert max_points_on_straight_line([(1, 0), (1, 4), (1, -1)]) == 3


def test_same_points():
    assert max_points_on_straight_line([(1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]) == 5


def test_negative_difference():
    assert max_points_on_straight_line([(4, -4), (8, -4), (-4, -4)]) == 3
    assert max_points_on_straight_line([(0, 0), (1, 1), (-1, -1)]) == 3


def test_foo():
    ls = [(-6, -17), (5, -16), (-18, -17), (2, -4), (5, -13), (-2, 20)]
    assert max_points_on_straight_line(ls) == 2
