def rearrange_array(arr):
    """
    Rearrange a given array so that arr[i] becomes arr[arr[i]]
    with O(1) extra space. The values in the array will become the new indizes.

    Time complexity: O(n + n)
    Space complexity: O(1)
    """
    n = len(arr)

    def is_encoded(num):
        return num >= n

    def encode(original_value, new_value):
        return n + n * original_value + new_value

    def decode(num):
        return ((num / n) - 1, num % n)

    def decode_new(num):
        return decode(num)[1]

    def decode_original(num):
        if is_encoded(num):
            return decode(num)[0]
        else:
            return num

    for i in range(0, len(arr)):
        new_value = decode_original(arr[arr[i]])
        arr[i] = encode(arr[i], new_value)

    for i in range(0, len(arr)):
        arr[i] = decode_new(arr[i])

    return arr


def test_rearrange_array():
    assert rearrange_array([0, 1]) == [0, 1]
    assert rearrange_array([1, 0]) == [0, 1]
    assert rearrange_array([2, 0, 1, 4, 3, 6, 5]) == [1, 2, 0, 3, 4, 5, 6]
    assert rearrange_array([0]) == [0]
    assert rearrange_array([]) == []
