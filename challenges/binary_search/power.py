"""
Implement pow(x, n) % d.
In other words, given x, n and d,
find x^n % d.
"""


def custom_pow(x, y):
    def multiply(a, b):
        return a * b
    return reduce(multiply, [x] * y, 1)


def find_pow(x, n, d):
    if n == 0:
        return 1 % d

    if x == 0:
        return 0

    n1 = n / 2
    n2 = n - n1

    pow1 = custom_pow(x, n1)
    if n2 > n1:
        pow2 = pow1 * x
    else:
        pow2 = pow1

    remainder1 = pow1 % d
    remainder2 = pow2 % d

    return (remainder1 * remainder2) % d


def test_custom_pow():
    assert custom_pow(3, 4) == pow(3, 4)


def test_find_pow():
    assert find_pow(2, 3, 3) == 2
    assert find_pow(4, 8, 5) == 1
    assert find_pow(7, 9, 4) == 3
    assert find_pow(0, 0, 1) == 0
    assert find_pow(-1, 1, 20) == 19
