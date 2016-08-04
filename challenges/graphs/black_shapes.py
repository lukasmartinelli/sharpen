import collections


def adjacent_black_fields(matrix, row_idx, col_idx):
    adjacent = [(row_idx + 1, col_idx), (row_idx - 1, col_idx),
                (row_idx, col_idx + 1), (row_idx, col_idx - 1)]

    def is_within_matrix(row_idx, col_idx):
        row_count = len(matrix)
        col_count = len(matrix[0])
        return 0 <= row_idx < row_count and 0 <= col_idx < col_count

    def is_black(row_idx, col_idx):
        return matrix[row_idx][col_idx] == 'X'

    return [f for f in adjacent if is_within_matrix(f[0], f[1]) and
            is_black(f[0], f[1])]


def find_black_fields(matrix):
    for row_idx, row in enumerate(matrix):
        for col_idx, field in enumerate(row):
            if field == 'X':
                yield (row_idx, col_idx)


def count_black_shapes(matrix):
    part_of_shape = {}

    def is_part_of_shape(row_idx, col_idx):
        return (row_idx, col_idx) in part_of_shape

    def mark_shape(row_idx, col_idx):
        part_of_shape[(row_idx, col_idx)] = True

        for row_idx, col_idx in adjacent_black_fields(matrix, row_idx, col_idx):
            if not is_part_of_shape(row_idx, col_idx):
                mark_shape(row_idx, col_idx)

    shape_count = 0
    for row_idx, col_idx in find_black_fields(matrix):
        if not is_part_of_shape(row_idx, col_idx):
            shape_count += 1
            mark_shape(row_idx, col_idx)

    return shape_count


def test_single_black_shape():
    matrix = ['XXX', 'XXX', 'XXX']
    assert count_black_shapes(matrix) == 1


def test_multipel_black_shape():
    matrix = ['OOOXOOO',
              'OOXXOXO',
              'OXOOOXO']
    assert count_black_shapes(matrix) == 3
