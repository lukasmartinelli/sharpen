def greatest_common_divisor(m, n):
    low = min(m, n)
    high = max(m, n)

    if low == 0:
        return high

    for divisor in reversed(xrange(1, low + 1)):
        if low % divisor == 0 and high % divisor == 0:
            return divisor

gcd = greatest_common_divisor
assert gcd(6, 9) == 3
assert gcd(9, 6) == 3
assert gcd(14, 6) == 2
assert gcd(1, 2) == 1
assert gcd(1, 1) == 1
assert gcd(1, 0) == 1
assert gcd(2, 0) == 2
