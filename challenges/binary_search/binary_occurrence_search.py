"""
Given a sorted array of integers, find the number of occurrences
of a given target value.
"""


def count_element(numbers, constraint):
    if len(numbers) == 0:
        return 0

    if len(numbers) == 1:
        if numbers[0] == constraint:
            return 1
        else:
            return 0

    half = len(numbers)/2
    if numbers[half] < constraint:
        return count_element(numbers[half:], constraint)
    elif numbers[half] > constraint:
        return count_element(numbers[:half], constraint)
    else:
        return 1 + count_element(numbers[:half], constraint) + count_element(numbers[half+1:], constraint)


def test_count_element():
    assert count_element([1, 1, 2, 3, 4, 5, 6], 1) == 2
    assert count_element([1, 1, 2, 3, 4, 5, 5, 5, 6], 5) == 3
