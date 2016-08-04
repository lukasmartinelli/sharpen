"""
Given an array of integers, every element appears twice except for one.
Find that single one.
"""
import math


def find_single_number(arr):
    single_number = 0

    for num in arr:
        mask = 1 << num
        single_number ^= mask

    return int(math.log(single_number, 2))


def test_find_single_number():
    assert find_single_number([1, 2, 2, 3, 1]) == 3
