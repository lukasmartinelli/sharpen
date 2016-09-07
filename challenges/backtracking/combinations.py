def combinations(n, k):
    """
    Given two integers n and k, return all possible combinations of k numbers
    out of 1 2 3 ... n.

        n = 4
        k = 2

        [
            [1,2],
            [1,3],
            [1,4],
            [2,3],
            [2,4],
            [3,4],
        ]
    """
    def find_combination(combination, nums):
        if len(combination) >= k:
            yield combination
            return

        for i, n in enumerate(nums):
            for c in find_combination(combination + [n], nums[i+1:]):
                yield c

    return list(find_combination([], range(1, n + 1)))


def test_combinations():
    assert combinations(4, 2) == [
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
        [3, 4],
    ]
