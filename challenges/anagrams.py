import collections


def anagram_id(word):
    return ''.join(sorted(word))


def anagrams(words):
    lookup = collections.OrderedDict()

    for idx, word in enumerate(words, start=1):
        word_id = anagram_id(word)

        if word_id in lookup:
            lookup[word_id] += [idx]
        else:
            lookup[word_id] = [idx]

    return lookup.values()


def test_anagrams():
    words = ["cat", "dog", "god", "tca"]
    assert anagrams(words) == [[1, 4], [2, 3]]


def test_with_no_anagrams():
    words = ["bub", "cat", "dog", "god", "tca"]
    assert anagrams(words) == [[1], [2, 5], [3, 4]]
