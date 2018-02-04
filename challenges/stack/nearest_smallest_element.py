def nearest_smallest_element(arr):
    """
    Given an array arr, find the nearest smaller element for each element.
    The index of the smaller element must be smaller than the current element.
    """
    smaller_numbers = []

    def nearest(n):
        def find_previous_num():
            for previous_num in reversed(smaller_numbers):
                if previous_num < n:
                    return previous_num
            return -1

        def append_smaller_number_before_preceding_big(n):
            while len(smaller_numbers) > 0 and smaller_numbers[-1] > n:
                smaller_numbers.pop()
            smaller_numbers.append(n)

        previous_num = find_previous_num()
        append_smaller_number_before_preceding_big(n)
        return previous_num

    return [nearest(n) for n in arr]


def test_nearest_smallest_element():
    assert nearest_smallest_element([4, 5, 2, 10, 12, 11] ) == [-1, 4, -1, 2, 10, 10]
    assert nearest_smallest_element([4]) == [-1]
    assert nearest_smallest_element([]) == []
