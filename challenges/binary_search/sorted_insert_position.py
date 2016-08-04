"""
Given a sorted array and a target value, return the index if the target is
found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
"""

def search_insert(arr, target):
    first = 0
    last = len(arr) - 1
    mid = 0

    while first <= last:
        mid = (first + last) / 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            first = mid + 1
        elif arr[mid] > target:
            last = mid - 1

    insertion_point = mid
    while insertion_point < len(arr) and arr[insertion_point] < target:
        insertion_point += 1

    return insertion_point


def test_binary_search():
    arr = [1, 3, 5, 6]
    assert search_insert(arr, 3) == 1
    arr = [1, 3, 4, 5, 6]
    assert search_insert(arr, 6) == 4


def test_insertion():
    arr = [1]
    assert search_insert(arr, 2) == 1

    arr = []
    assert search_insert(arr, 2) == 0

    arr = [3]
    assert search_insert(arr, 2) == 0

    arr = [1, 3]
    assert search_insert(arr, 3) == 1

    arr = [1, 3, 5, 6]
    assert search_insert(arr, 2) == 1

    arr = [1, 3, 5, 6]
    assert search_insert(arr, 7) == 4
