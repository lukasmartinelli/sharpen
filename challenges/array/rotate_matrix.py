def rotate_matrix(matrix):
    """
    Rotate the n x n matrix 90 degrees clockwise.

    Given the original matrix.

        initial_matrix = [
            [1, 2],
            [3, 4]
        ]

    The rotated matrix should look like this.

        rotated_matrix = [
            [3, 1],
            [4, 2]
        ]
    """
    n = len(matrix)
    new_matrix = [[0] * n for i in range(0, n)]

    def calculate_new_matrix_index(old_y, old_x):
        return (old_x, n - 1 - old_y)

    for y in range(0, n):
        for x in range(0, n):
            new_y, new_x = calculate_new_matrix_index(y, x)
            new_matrix[new_y][new_x] = matrix[y][x]

    return new_matrix


def test_rotate_matrix():
    initial_matrix = [
          [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]
        ]

    rotated_matrix = [
          [13, 9, 5, 1],
          [14, 10, 6, 2],
          [15, 11, 7, 3],
          [16, 12, 8, 4]
        ]
    assert rotate_matrix(initial_matrix) == rotated_matrix
