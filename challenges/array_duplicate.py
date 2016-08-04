import collections


def find_duplicate(arr):
    """
    Find the first duplicate in an array of n + 1 integers between 1 and n.
    Find a repeating number in linear time using less than O(n) space and
    traversing the array only once.

    Given the input A.

        assert find_duplicate([3, 4, 1, 4, 1]) == 1
    """
    counts = collections.defaultdict(int)

    for elem in arr:
        counts[elem] += 1

        if counts[elem] > 1:
            return elem


def test_find_duplicate_in_single_element_list():
    assert find_duplicate([4]) is None


def test_find_duplicate_in_short_list():
    assert find_duplicate([3, 4, 1, 4, 1]) == 4


def test_find_duplicate_in_large_list():
    assert find_duplicate(range(0, 200) + [4]) == 4
