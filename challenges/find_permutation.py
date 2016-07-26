"""
Given a positive integer n and a string s consisting only letters D or I,
you have to find any permutation of first n positive integer that satisfy
the given input string.

D means the next number is smaller, while I means the next number is greater.
"""

import collections


def find_permutation(s, n):
    choices = collections.deque(range(1, n + 1))

    def next_is_smaller(c):
        return c == 'D'

    def next_is_greater(c):
        return c == 'I'

    for condition in s:
        if next_is_smaller(condition):
            yield choices.pop()
        elif next_is_greater(condition):
            yield choices.popleft()

    yield choices.pop()


def test_permutations():
    assert list(find_permutation('IDIDI', 6)) == [1, 6, 2, 5, 3, 4]
    assert list(find_permutation('I', 2)) == [1, 2]
    assert list(find_permutation('ID', 3)) == [1, 3, 2]
    assert list(find_permutation('IDD', 4)) == [1, 4, 3, 2]
    assert list(find_permutation('IDDI', 5)) == [1, 5, 4, 2, 3]
    assert list(find_permutation('DIDI', 5)) == [5, 1, 4, 2, 3]
    assert list(find_permutation('IDDID', 6)) == [1, 6, 5, 2, 4, 3]
