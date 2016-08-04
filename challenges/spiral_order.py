def spiral_order(matrix):
    """
    Return m * n matrix in spiral order.

    Given the following matrix.

        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

    The spiral order of the matrix.

        spiral_order = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    """
    m = len(matrix)
    if m == 0:
        return

    n = len(matrix[0])
    if n == 0:
        return

    if n == 1:
        for row in matrix:
            yield row[0]
        return

    if m == n == 1:
        yield matrix[0][0]
        return

    # Upper outer shell
    for column in matrix[0]:
        yield column

    # Right outer shell
    for row in matrix[1:-1]:
        yield row[-1]

    if m > 1:
        # Lower outer shell
        for column in reversed(matrix[-1]):
            yield column

    # Left outer shell
    for row in list(reversed(matrix))[1:-1]:
        yield row[0]

    # Peel off the shell
    inner_matrix = [row[1:-1] for row in matrix[1:-1]]
    for num in spiral_order(inner_matrix):
        yield num


def test_spiral_order_single_elem():
    assert list(spiral_order([
        [1]
    ])) == [1]


def test_spiral_order_single_row():
    assert list(spiral_order([
        [1],
        [2],
        [3]
    ])) == [1, 2, 3]


def test_spiral_order():
    assert list(spiral_order([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
