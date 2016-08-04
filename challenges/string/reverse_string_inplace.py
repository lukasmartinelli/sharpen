def reverse(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1

    return arr


def test_reverse():
    assert reverse(['h', 'e', 'l', 'l']) == ['l', 'l', 'e', 'h']
    assert reverse(['h', 'e', 'y', 'w', 'o']) == ['o', 'w', 'y', 'e', 'h']
