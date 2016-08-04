"""
Given an array of integers, sort the array into a wave
like array and return it.

Arrange the elements into a sequence such that `a1 >= a2 <= a3 >= a4 <= a5`
"""


def wave(numbers):
    # O(n log n)
    sorted_numbers = sorted(numbers)

    # Go through numbers
    # On uneven idx choose the previous number
    # On even idx choose the next number

    for idx in range(0, len(numbers)):
        if idx % 2 == 0:
            if idx == len(numbers) - 1:
                yield sorted_numbers[idx]
            else:
                yield sorted_numbers[idx+1]
        else:
            yield sorted_numbers[idx-1]


def test_wave():
    numbers = [4, 3, 2, 1]
    assert list(wave(numbers)) == [2, 1, 4, 3]


def test_longer_wave():
    numbers = [8, 4, 6, 7, 3, 2, 1, 5]
    assert list(wave(numbers)) == [2, 1, 4, 3, 6, 5, 8, 7]


def test_uneven_wave():
    numbers = [4, 3, 2, 1, 5]
    assert list(wave(numbers)) == [2, 1, 4, 3, 5]
