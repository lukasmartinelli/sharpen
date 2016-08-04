"""
Find the trailing zeros in factorial.
Given an integer n, return the number of trailing zeroes in n!.
"""


def factorial(n):
    "Time complexity is O(n)"
    result = n
    while n > 1:
        n -= 1
        result *= n
    return result


def trailing_zeros(n):
    "Time complexity is O(n) in worst case"
    zeros = 0
    while n % 10 == 0:
        n /= 10
        zeros += 1
    return zeros


def trailing_zeros_factorial(n):
    zeros = 0
    exponent = 1

    while n / pow(5, exponent) > 0:
        zeros += n / pow(5, exponent)
        exponent += 1

    return zeros


def test_factorial():
    assert factorial(5) == 5 * 4 * 3 * 2 * 1


def test_trailing_zeros():
    assert trailing_zeros(120) == 1
    assert trailing_zeros(500) == 2
    assert trailing_zeros(factorial(5)) == 1
    assert trailing_zeros_factorial(5) == 1
    assert trailing_zeros_factorial(7927) == 1979
    assert trailing_zeros_factorial(4617) == 1151
