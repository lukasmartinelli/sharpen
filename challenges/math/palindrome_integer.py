"""
Determine whether an integer is a palindrome. Do this without extra space.

A palindrome integer is an integer x for which reverse(x) = x where reverse(x)
is x with its digit reversed. Negative numbers are not palindromic.

For example the integer 12321 is palindromic while 12312 is not.
"""


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


def test_integer_len():
    assert integer_len(3) == 1
    assert integer_len(12345) == 5


def test_is_integer_palindrom_for_negative_number():
    assert not is_integer_palindrom(-1)


def test_is_integer_palindrom():
    assert not is_integer_palindrom(12341)
    assert is_integer_palindrom(123321)
    assert is_integer_palindrom(5412145)
    assert is_integer_palindrom(11)
