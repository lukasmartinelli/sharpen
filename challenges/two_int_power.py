import sys


def power_of_two(n):
    """
    Given a positive integer which fits in a 32 bit signed integer,
    find if it can be expressed as A^P where P > 1 and A > 0. A and P
    both should be integers.
    """
    if n == 0 or n == 1:
        return True

    for p in range(2, 32):
        for a in range(1, int(pow(sys.maxint, 1.0 / p))):
            print(a, p)
            if pow(a, p) == n:
                return True

    return False

assert power_of_two(4)
assert power_of_two(1)
assert not power_of_two(2)
assert not power_of_two(3)
assert not power_of_two(5)
assert not power_of_two(6)
assert not power_of_two(7)
assert power_of_two(8)
assert power_of_two(9)
assert not power_of_two(10)
assert not power_of_two(11)
assert not power_of_two(12)
assert not power_of_two(13)
assert not power_of_two(14)
assert not power_of_two(15)
assert power_of_two(16)
assert not power_of_two(17)
assert not power_of_two(18)
assert not power_of_two(19)
assert not power_of_two(21)
assert not power_of_two(22)
assert not power_of_two(23)
assert not power_of_two(24)
assert power_of_two(25)
assert not power_of_two(26)
assert power_of_two(27)
assert not power_of_two(28)
assert not power_of_two(29)
assert not power_of_two(30)
assert not power_of_two(31)
assert power_of_two(32)
assert power_of_two(1024000000)
