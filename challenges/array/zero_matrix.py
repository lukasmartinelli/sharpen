def zero_matrix(matrix):
    """
    Given an m x n matrix of 0s and 1s, if an element is 0,
    set its entire row and column to 0.

    Given a matrix A as input.

        A = [[1, 0, 1],
             [1, 1, 1],
             [1, 1, 1]]

    On returning the matrix A should have the rows and columns
    containing the initial 0 all set to 0.

        A = [[0, 0, 0],
             [1, 0, 1],
             [1, 0, 1]]
    """
    m = len(matrix)
    n = len(matrix[0])

    # Space complexity is O(m) + O(n)
    zero_columns = {}
    zero_rows = {}

    # Time complexity is O(m * n)
    for y, row in enumerate(matrix):
        for x, col in enumerate(row):
            if col == 0:
                zero_rows[y] = True
                zero_columns[x] = True

    for y in zero_rows.keys():
        for x in range(0, n):
            matrix[y][x] = 0

    for x in zero_columns.keys():
        for y in range(0, m):
            matrix[y][x] = 0

    return matrix


def test_zero_matrix_single_value():
    assert zero_matrix([[0]]) == [[0]]


def test_zero_matrix_two_rows_three_cols():
    assert zero_matrix([
         [1, 1, 1],
         [1, 1, 0]
    ]) == [
         [1, 1, 0],
         [0, 0, 0]
    ]


def test_zero_matrix_three_rows_cols():
    assert zero_matrix([
         [1, 1, 1],
         [0, 1, 0],
         [1, 1, 1]
    ]) == [
         [0, 1, 0],
         [0, 0, 0],
         [0, 1, 0]
    ]
