"""Implement square root"""


def binary_sqrt_search(num):
    first = 0
    last = num

    while first <= last:
        mid = (first + last) / 2

        pow2 = mid * mid
        if pow2 == num:
            return mid

        if pow2 < num:
            first = mid + 1

        if pow2 > num:
            last = mid - 1

    return last


def sqrt(num):
    return binary_sqrt_search(num)

assert sqrt(3) == 1
assert sqrt(0) == 0
assert sqrt(1) == 1
assert sqrt(4) == 2
assert sqrt(8) == 2
assert sqrt(9) == 3
assert sqrt(16) == 4
assert sqrt(25) == 5
assert sqrt(26) == 5
assert sqrt(308634616) == 17567
