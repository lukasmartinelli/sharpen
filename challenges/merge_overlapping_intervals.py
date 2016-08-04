class Interval:
    "Interval spans from start over to end"
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def merge(self, other):
        "Merge interval with other interval and return merged interval"
        return Interval(
            min(self.start, other.start),
            max(self.end, other.end)
        )

    def __repr__(self):
        return '({},{})'.format(self.start, self.end)


def merge_overlapping_intervals(intervals):
    """
    Given a collection of intervals, merge all overlapping intervals.

    Given the list of intervals A.

        A = [Interval(1, 3), Interval(2, 6),
             Interval(8, 10), Interval(15, 18)]

    The function should return the list of merged intervals.

        A = [Interval(1, 6), Interval(8, 10), Interval(15, 18)]
    """
    intervals.sort(key=lambda i: i.start)
    if len(intervals) == 0:
        return intervals

    merged_intervals = [intervals.pop(0)]

    # O(n)
    while len(intervals) > 0:
        prev_interval = merged_intervals[-1]
        interval = intervals.pop(0)

        if prev_interval.end >= interval.start:
            merged_intervals[-1] = prev_interval.merge(interval)
        else:
            merged_intervals.append(interval)

    return merged_intervals


def test_merge_overlapping_intervals():
    intervals = [(47, 76), (51, 99), (28, 78), (54, 94),
                 (12, 72), (31, 72), (12, 55), (24, 40),
                 (59, 79), (41, 100), (46, 99), (5, 27),
                 (13, 23), (9, 69), (39, 75), (51, 53),
                 (81, 98), (14, 14), (27, 89), (73, 78),
                 (28, 35), (19, 30), (39, 87), (60, 94),
                 (71, 90), (9, 44), (56, 79), (58, 70),
                 (25, 76), (18, 46), (14, 96), (43, 95),
                 (70, 77), (13, 59), (52, 91), (47, 56),
                 (63, 67), (28, 39), (51, 92), (30, 66),
                 (4, 4), (29, 92), (58, 90), (6, 20),
                 (31, 93), (52, 75), (41, 41), (64, 89),
                 (64, 66), (24, 90), (25, 46), (39, 49),
                 (15, 99), (50, 99), (9, 34), (58, 96),
                 (85, 86), (13, 68), (45, 57), (55, 56),
                 (60, 74), (89, 98), (23, 79), (16, 59),
                 (56, 57), (54, 85), (16, 29), (72, 86),
                 (10, 45), (6, 25), (19, 55), (21, 21),
                 (17, 83), (49, 86), (67, 84), (8, 48),
                 (63, 85), (5, 31), (43, 48), (57, 62),
                 (22, 68), (48, 92), (36, 77), (27, 63),
                 (39, 83), (38, 54), (31, 69), (36, 65),
                 (52, 68)]

    intervals = [Interval(i[0], i[1]) for i in intervals]
    merged_intervals = merge_overlapping_intervals(intervals)
    merged_intervals = [(i.start, i.end) for i in merged_intervals]
    assert merged_intervals == [(4, 4), (5, 100)]
