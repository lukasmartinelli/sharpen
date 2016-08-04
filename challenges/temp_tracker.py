import collections


class TempTracker:
    """
    Temperature tracker to calculate mean, mode, min, max of temperature
    events. Favor speeding up the getter functions over speeding
    up the insert() function.
    """
    def __init__(self):
        self._max_temp = 0
        self._min_temp = 0
        self._temp_sum = 0
        self._temp_count = 0
        self._temps = collections.defaultdict(lambda: 0)

    def __str__(self):
        return '\n'.join([
            'Max: ' + str(self.max),
            'Min: ' + str(self.min),
            'Mean: ' + str(self.mean),
            'Mode: ' + str(self.mode),
        ])

    def insert(self, temp):
        "O(1)"
        self._max_temp = max(self._max_temp, temp)
        self._min_temp = min(self._min_temp, temp)

        self._temps[temp] += 1
        self._temp_sum += temp
        self._temp_count += 1

    @property
    def min(self):
        "O(1)"
        return self._min_temp

    @property
    def max(self):
        "O(1)"
        return self._max_temp

    @property
    def mean(self):
        "O(1)"
        return self._temp_sum / self._temp_count

    @property
    def mode(self):
        "O(n)"
        mode = self._temps.keys()[0]
        max_count = 0
        for temp, count in self._temps.items():
            if count > max_count:
                max_count = count
                mode = temp

        return mode


def test_temptracker():
    tracker = TempTracker()
    tracker.insert(1)
    tracker.insert(3)
    tracker.insert(3)
    tracker.insert(4)
    tracker.insert(5)
    tracker.insert(-2)

    assert tracker.max == 5
    assert tracker.min == -2
    assert tracker.mean == 2
    assert tracker.mode == 3
