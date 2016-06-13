def length_longest_substring(text):
    max_length = start = 0
    used_chars = {}

    for i, c in enumerate(text):
        if c in used_chars and start <= used_chars[c]:
            start = used_chars[c] + 1
        else:
            max_length = max(max_length, i - start + 1)

        used_chars[c] = i

    return max_length


def test_length_longest_substring():
    assert length_longest_substring("") == 0
    assert length_longest_substring("u") == 1
    assert length_longest_substring("bbbbb") == 1
    assert length_longest_substring("abcabcbb") == 3
