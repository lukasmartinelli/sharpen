def binary_search_rotated(arr, n):
    first = 0
    last = len(arr) - 1

    while first <= last:
        mid = (first + last) / 2
        print('Search from arr[{}] to arr[{}] with mid arr[{}]'.format(first, last, mid))

        if arr[mid] == n:
            return mid
        # is left sorted
        elif arr[first] < arr[mid]:
            if n >= arr[first] and n < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
        # is right sorted
        else:
            if n > arr[mid] and n <= arr[last]:
                first = mid + 1
            else:
                last = mid - 1

    return -1


def test_binary_search_rotated():
    assert binary_search_rotated([
        101, 103, 106, 109, 158, 164, 182, 187, 202,
        205, 2, 3, 32, 57, 69, 74, 81, 99, 100
    ], 202) == 8
    assert binary_search_rotated([4, 5, 3], 3) == 2
    assert binary_search_rotated([5, 4], 4) == 1
    assert binary_search_rotated([4, 6, 7, 8, 9, 0, 2], 9) == 4
    assert binary_search_rotated([8, 9, 0, 2, 4, 6, 7], 9) == 1
    assert binary_search_rotated([8, 9, 0, 2, 4, 6, 7], 6) == 5
    assert binary_search_rotated([8, 9, 0, 2, 4, 6, 7], 10) == -1
    assert binary_search_rotated([4, 5, 6, 7, 0, 1, 2], 1) == 5
    assert binary_search_rotated([4], 1) == -1
