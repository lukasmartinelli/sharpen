""""
PAYPALISHIRING

P.......A........H.......N....
..A..P....L....S....I...I....G
....Y.........I........R......
"""


"""
ABCD

A....C..
...B....D
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

assert convert_text_zigzag_pattern("HEYMAN", 1) == "HEYMAN"
assert convert_text_zigzag_pattern("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert convert_text_zigzag_pattern("ABCD", 2) == "ACBD"
