def pascal_triangle(num_rows):
    """
    Calculate the pascal triangle for a given number of rows.
    """
    def get_elem(arr, idx, default):
        if idx < 0 or idx >= len(arr):
            return default
        else:
            return arr[idx]

    def generate_columns(previous_row, num_columns):
        for col_idx in range(0, num_columns):
            yield (
                get_elem(previous_row, col_idx-1, 0) +
                get_elem(previous_row, col_idx, 0)
            )

    if num_rows == 0:
        return []

    rows = [[1]]

    for row_idx in range(1, num_rows):
        prev = rows[row_idx-1]
        rows.append(list(generate_columns(prev, row_idx+1)))

    return rows


def test_pascal_triangle():
    triangle = pascal_triangle(5)
    assert triangle == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]
