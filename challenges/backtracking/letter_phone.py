digit_lookup = {
    '0': ['0'],
    '1': ['1'],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


def letter_combinations(digits):
    return list(possible_combination(digits, []))


def possible_combination(digits, combination):
    if len(digits) > 0:
        digit = digits[0]

        for letter in digit_lookup[digit]:
            new_combination = combination + [letter]
            for c in possible_combination(digits[1:], new_combination):
                yield ''.join(c)
    else:
        yield ''.join(combination)


def test_combination():
    assert letter_combinations("23") == [
        "ad", "ae", "af", "bd", "be",
        "bf", "cd", "ce", "cf"
    ]

    assert letter_combinations("1589") == [
        "1jtw", "1jtx", "1jty", "1jtz", "1juw", "1jux", "1juy", "1juz",
        "1jvw", "1jvx", "1jvy", "1jvz", "1ktw", "1ktx", "1kty", "1ktz",
        "1kuw", "1kux", "1kuy", "1kuz", "1kvw", "1kvx", "1kvy", "1kvz",
        "1ltw", "1ltx", "1lty", "1ltz", "1luw", "1lux", "1luy", "1luz",
        "1lvw", "1lvx", "1lvy", "1lvz"
    ]
