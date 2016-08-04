"""
Given a sorted array of integers, find the starting and ending position
of a given target value.
"""


def search_last_occurrence(arr, target):
    first = 0
    last = len(arr) - 1

    found = -1
    while first <= last:
        mid = (first + last) / 2
        if arr[mid] == target:
            found = mid
            first = mid + 1
        if arr[mid] < target:
            first = mid + 1
        if arr[mid] > target:
            last = mid - 1

    return found


def search_first_occurrence(arr, target):
    first = 0
    last = len(arr) - 1

    found = -1
    while first <= last:
        mid = (first + last) / 2
        if arr[mid] == target:
            found = mid
            last = mid - 1
        if arr[mid] < target:
            first = mid + 1
        if arr[mid] > target:
            last = mid - 1

    return found


def search_range(arr, target):
    left = search_first_occurrence(arr, target)
    right = search_last_occurrence(arr, target)

    return [left, right]


def test_first_search_occurrence():
    arr = [5, 7, 7, 7, 7, 7, 8, 8, 10]
    assert search_first_occurrence(arr, 7) == 1
    assert search_first_occurrence(arr, 8) == 6


def test_last_search_occurrence():
    arr = [5, 7, 7, 7, 7, 7, 8, 8, 10]
    assert search_last_occurrence(arr, 7) == 5
    assert search_last_occurrence(arr, 8) == 7


def test_search_range():
    arr = [5, 7, 7, 8, 8, 10]
    assert search_range(arr, 4) == [-1, -1]
    assert search_range(arr, 5) == [0, 0]
    assert search_range(arr, 7) == [1, 2]
    assert search_range(arr, 8) == [3, 4]
    assert search_range(arr, 10) == [5, 5]
