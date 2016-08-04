COLUMN_ENCODING = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26
}


def column_number(column_name):
    """
    Given a column title as appears in an Excel sheet,
    return its corresponding column number.
    """
    num = 0
    for c, n in zip(column_name, reversed(range(0, len(column_name)))):
        num += COLUMN_ENCODING[c] * pow(len(COLUMN_ENCODING), n)

    return num


def test_column_number():
    assert column_number('A') == 1
    assert column_number('Z') == 26
    assert column_number('AA') == 27
    assert column_number('AB') == 28
    assert column_number('AAB') == 704
