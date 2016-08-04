"""
Given an unsorted array.

    elements = [1, 10, 5]

Find the maximum difference between the
successive elements in its sorted form.

    # max difference is between 5 and 10
    assert max_gap(elements) == 5

You may assume that all the elements in the array are
non-negative integers and fit in the 32-bit signed integer range.
You may also assume that the difference will not overflow.
"""


def max_gap(numbers):
    # O(n * log(n))
    numbers = sorted(numbers)
    # O(n)
    max_diff = 0
    for prev, cur in zip(numbers, numbers[1:]):
        diff = abs(cur - prev)
        max_diff = max(max_diff, diff)

    return max_diff


def test_max_gap():
    assert max_gap([1]) == 0
    assert max_gap([1, 10]) == 9
    assert max_gap([7, 5]) == 2
    assert max_gap([1, 10, 5]) == 5
