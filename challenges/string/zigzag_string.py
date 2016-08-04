""""
The string 'ABCD' is written in a zigzag pattern on a given number
of rows like this.

    A....C..
    ...B....D

Write the code that will take a string and make this conversion given a
number of rows.
"""


def convert_text_zigzag_pattern(text, num_rows):
    if num_rows == 1:
        return text

    def zigzag():
        for i in xrange(0, num_rows):
            yield i

        for i in reversed(xrange(1, num_rows - 1)):
            yield i

        for i in zigzag():
            yield i

    def distribute_chars_on_rows():
        rows = [[] for _ in range(0, num_rows)]
        for char, row_idx in zip(text, zigzag()):
            arr = rows[row_idx]
            arr.append(char)
        return [''.join(r) for r in rows]

    return ''.join(distribute_chars_on_rows())


def test_convert_text_zigzag_pattern():
    assert convert_text_zigzag_pattern("HEYMAN", 1) == "HEYMAN"
    assert convert_text_zigzag_pattern("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert convert_text_zigzag_pattern("ABCD", 2) == "ACBD"
