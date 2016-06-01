def zero_matrix(matrix):
    """
    Given an m x n matrix of 0s and 1s, if an element is 0,
    set its entire row and column to 0.
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

assert zero_matrix([[0]]) == [[0]]
assert zero_matrix([
     [1, 1, 1],
     [1, 1, 0]
]) == [
     [1, 1, 0],
     [0, 0, 0]
]

assert zero_matrix([
     [1, 1, 1],
     [0, 1, 0],
     [1, 1, 1]
]) == [
     [0, 1, 0],
     [0, 0, 0],
     [0, 1, 0]
]
