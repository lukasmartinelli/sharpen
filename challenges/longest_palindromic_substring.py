"""
Given a string S, find the longest palindromic substring in S.
"""


import itertools
import collections


def is_palindrome(word):
    for c1, c2 in itertools.izip(word, reversed(word)):
        if c1 != c2:
            return False
    return True


def longest_palindromic_substring(sentence):
    reverse_lookup = collections.defaultdict(list)
    max_palindrome = sentence[0]

    # build up lookup O(n)
    for i in reversed(range(0, len(sentence))):
        c = sentence[i]
        reverse_lookup[c].append(i)

    # start going through
    for i in range(0, len(sentence)):
        c1 = sentence[i]
        for j in reverse_lookup[c1]:
            if j > i and j + 1 - i > len(max_palindrome):
                c2 = sentence[j]
                if c1 == c2:
                    word = sentence[i:j+1]
                    if is_palindrome(word):
                        max_palindrome = word

    return max_palindrome


def test_longest_palindromic_substring():
    lps = longest_palindromic_substring
    assert lps('aaaabaaa') == 'aaabaaa'
    assert lps('faxalaxabx') == 'axalaxa'
    assert lps('hululxlaluh') == 'ulu'
    assert is_palindrome('aba')
    assert not is_palindrome('abac')
    assert lps('aba') == 'aba'
    assert lps('ab') == 'a'
