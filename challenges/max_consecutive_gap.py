def max_gap(numbers):
    # O(n * log(n))
    numbers = sorted(numbers)
    # O(n)
    max_diff = 0
    for prev, cur in zip(numbers, numbers[1:]):
        diff = abs(cur - prev)
        max_diff = max(max_diff, diff)

    return max_diff


def test_gap():
    assert max_gap([1, 10]) == 9
    assert max_gap([1]) == 0
    assert max_gap([7, 5]) == 2
    assert max_gap([1, 10, 5]) == 5
