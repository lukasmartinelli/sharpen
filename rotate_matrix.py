def rotate_matrix_not_in_place(matrix):
    "Complexity for n x n matrix is O(n^2) space and O(n^2) space"
    n = len(matrix)
    new_matrix = [[0] * n for i in range(0, n)]

    def calculate_new_matrix_index(old_y, old_x):
        return (old_x, n - 1 - old_y)

    for y in range(0, n):
        for x in range(0, n):
            new_y, new_x = calculate_new_matrix_index(y, x)
            new_matrix[new_y][new_x] = matrix[y][x]

    return new_matrix

def rotate_matrix(matrix):
    "Complexity for n x n matrix is O(n^2) space and O(n^2) space"
    n = len(matrix)
    #new_matrix = [[0] * n for i in range(0, n)]

    def calculate_new_matrix_index(old_y, old_x):
        return (old_x, n - 1 - old_y)

    def calculate_old_matrix_index(new_y, new_x):
        return (n - 1 - new_x, new_y)

    def calculate_swap_from_old(y):
        """
        Calculate the x idx depending from y at which
        the values must be taken from old idx
        """
        if y <= 1:
            return n - 1
        else:
            return n - y

    for y in range(0, n):
        for x in range(0, n):
            new_y, new_x = calculate_new_matrix_index(y, x)


            #print("({0}, {1}) => ({2}, {3}), {4}".format(y, x, new_y, new_x, calculate_swap_from_old(y)))
            if x >= calculate_swap_from_old(y):
                old_y, old_x = calculate_old_matrix_index(y, x)
                print('Replace old {} at ({}, {}) with {} from ({}, {})'.format(
                    matrix[new_y][new_x], new_y, new_x,
                    matrix[old_y][old_x], old_y, old_x
                ))
                matrix[new_y][new_x] = matrix[old_y][old_x]
            else:
                print('Replace new {} at ({}, {}) with {} from ({}, {})'.format(
                    matrix[new_y][new_x], new_y, new_x,
                    matrix[y][x], y, x
                ))
                tmp = matrix[new_y][new_x]
                matrix[new_y][new_x] = matrix[y][x]
                matrix[y][x] = tmp

    return matrix


assert rotate_matrix_not_in_place([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16]
]) == [
  [13, 9, 5, 1],
  [14, 10, 6, 2],
  [15, 11, 7, 3],
  [16, 12, 8, 4]
]

"""
Transformation pattern for 4x4 Matrix

(y, x) => (y, x)

(0, 0) => (0, 3), f, t
(0, 1) => (1, 3), f, t
(0, 2) => (2, 3), f, t
(0, 3) => (3, 3), t, t

(1, 0) => (0, 2), f,
(1, 1) => (1, 2), f
(1, 2) => (2, 2), f
(1, 3) => (3, 2), t

(2, 0) => (0, 1), f
(2, 1) => (1, 1), f
(2, 2) => (2, 1), t
(2, 3) => (3, 1), t

(3, 0) => (0, 0), f
(3, 1) => (1, 0), t
(3, 2) => (2, 0), t
(3, 3) => (3, 0), t
"""


"""
Transformation pattern for 3 x 3

(y, x) => (y, x)

(0, 0) => (0, 2), f
(0, 1) => (1, 2), f
(0, 2) => (2, 2), t

(1, 0) => (0, 1), f
(1, 1) => (1, 1), f
(1, 2) => (2, 1), t

(2, 0) => (0, 0), f
(2, 1) => (1, 0), t
(2, 2) => (2, 0), t
"""

"""
assert rotate_matrix([
  [1, 2],
  [3, 4]
]) == [
  [3, 1],
  [4, 2]
]

assert rotate_matrix([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]) == [
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]
"""
