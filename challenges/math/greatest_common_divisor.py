def greatest_common_divisor(m, n):
    """
    Using the Euclidean algorithm
    https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
    """
    low = min(m, n)
    high = max(m, n)

    if low == 0:
        return high

    remainder = high % low
    return greatest_common_divisor(low, remainder)


def test_greatest_common_divisor():
    gcd = greatest_common_divisor
    assert gcd(6, 9) == 3
    assert gcd(9, 6) == 3
    assert gcd(14, 6) == 2
    assert gcd(1, 2) == 1
    assert gcd(1, 1) == 1
    assert gcd(1, 0) == 1
    assert gcd(2, 0) == 2
    assert gcd(270, 192) == 6
