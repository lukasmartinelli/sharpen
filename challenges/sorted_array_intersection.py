
def intersection(arr_a, arr_b):
    """
    Given 2 sorted arrays, find all the elements
    which occur in both the arrays.
    """
    i = 0
    j = 0

    while i < len(arr_a) and j < len(arr_b):
        # print('a[{}] == b[{}] -> {} == {}'.format(i, j, arr_a[i], arr_b[j]))
        if arr_a[i] == arr_b[j]:
            yield arr_a[i]
            i += 1
            j += 1
        elif arr_a[i] > arr_b[j]:
            j += 1
        elif arr_a[i] < arr_b[j]:
            i += 1


assert list(intersection([1, 2, 3, 3, 4, 5, 6], [3, 3, 5])) == [3, 3, 5]
assert list(intersection([1, 2, 3, 3, 4, 5, 6], [3, 5])) == [3, 5]
assert list(intersection([], [])) == []
assert list(intersection([2], [-1, 0, 2])) == [2]
assert list(intersection([1, 2, 3, 4], [2, 3, 4])) == [2, 3, 4]
