import collections


def majority_element(arr):
    """
    Given an array of size n, find the majority element.
    The majority element is the element that appears
    more than floor(n/2) times.
    """
    counts = collections.defaultdict(int)
    for elem in arr:
        counts[elem] += 1
        if counts[elem] > len(arr) / 2:
            return elem


def test_majority_elemen():
    assert majority_element([2, 1, 2]) == 2
