import collections


class TempTracker:
    "Space complexity is O(n) where n is the number of unique temperatures"
    def __init__(self):
        self._max_temp = 0
        self._min_temp = 0
        self._temp_sum = 0
        self._temp_count = 0
        self._temps = collections.defaultdict(lambda: 0)

    def __str__(self):
        return '\n'.join([
            'Max: ' + str(self.get_max()),
            'Min: ' + str(self.get_min()),
            'Mean: ' + str(self.get_mean()),
            'Mode: ' + str(self.get_mode()),
        ])

    def insert(self, temp):
        "O(1)"
        self._max_temp = max(self._max_temp, temp)
        self._min_temp = min(self._min_temp, temp)

        self._temps[temp] += 1
        self._temp_sum += temp
        self._temp_count += 1

    def get_min(self):
        "O(1)"
        return self._min_temp

    def get_max(self):
        "O(1)"
        return self._max_temp

    def get_mean(self):
        "O(1)"
        return self._temp_sum / self._temp_count

    def get_mode(self):
        "O(n)"
        mode = self._temps.keys()[0]
        max_count = 0
        for temp, count in self._temps.items():
            if count > max_count:
                max_count = count
                mode = temp

        return mode


tracker = TempTracker()
tracker.insert(1)
tracker.insert(3)
tracker.insert(3)
tracker.insert(4)
tracker.insert(5)
tracker.insert(-2)
print(tracker)
