def pow_mod(x, n, m):
    if n == 0:
        return 1 % m
    elif n % 2 == 0:
        y = pow_mod(x, n/2, m)
        return (y * y) % m
    else:
        y = x % m
        return (y * pow_mod(x, n-1, m)) % m


def test_pow_mod():
    assert pow_mod(0, 0, 1) == 0
    assert pow_mod(2, 3, 3) == 2
    assert pow_mod(71045970, 41535484, 64735492) == 20805472
