def integer_len(n):
    length = 1
    while n / 10 > 0:
        n /= 10
        length += 1
    return length


def is_integer_palindrom(n):
    if n < 0:
        return False

    length = integer_len(n)
    while True:
        if length < 2:
            return True

        first_digit = n / (pow(10, length - 1))
        last_digit = n % 10

        if first_digit == last_digit:
            n -= first_digit * pow(10, length - 1)
            n /= 10
            length -= 2
        else:
            return False

assert integer_len(3) == 1
assert integer_len(12345) == 5
assert not is_integer_palindrom(12341)
assert is_integer_palindrom(123321)
assert is_integer_palindrom(5412145)
assert is_integer_palindrom(11)
assert not is_integer_palindrom(-1)
