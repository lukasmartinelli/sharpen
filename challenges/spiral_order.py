"""
Example 1:

matrix_1 = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

Go down the spiral order 1st call.

order_1 = [1, 2, 3, 6, 9, 8, 7, 4]
inner_matrix_1 = [
    [ 5 ],
]

Go down the spiral order 2nd call.
Base case is reached because m == n == 1
order = [5]

Example 2:

matrix_2 = [
    [  1,  2,  3,  4,  5,  6 ],
    [  7,  8,  9, 10, 11, 12 ],
    [ 13, 14, 15, 16, 17, 18 ]
]

Go down the spiral order 1st call.

order_2 = [1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7]
inner_matrix_2 = [
    [ 8,  9, 10, 11 ]
]

Go down the spiral order 2nd call.
Now this is dangerous because the last row equals
the first row as well.

"""


def spiral_order(matrix):
    "Return m * n matrix in spiral order"
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
    # [ x, x, x ],
    # [ x, 5, x ],
    # [ x, x, x ]
    inner_matrix = [row[1:-1] for row in matrix[1:-1]]
    for num in spiral_order(inner_matrix):
        yield num
print(list(spiral_order([
    [1]
])))

print(list(spiral_order([
    [1],
    [2],
    [3]
])))

print(list(spiral_order([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])))

print(list(spiral_order([
    [1, 2, 3,  4,  5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18]
])))
