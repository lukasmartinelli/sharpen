import collections


def find_duplicate(arr):
    counts = collections.defaultdict(int)

    for elem in arr:
        counts[elem] += 1

        if counts[elem] > 1:
            return elem


assert find_duplicate([4]) is None
assert find_duplicate([3, 4, 1, 4, 1]) == 4
assert find_duplicate(range(0, 200) + [4]) == 4
