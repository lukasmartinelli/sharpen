def length_longest_substring(text):
    longest_substring = 0
    for i, from_char in enumerate(text):
        unique_chars = {}

        for j, to_char in enumerate(text[i:]):
            if to_char in unique_chars:
                longest_substring = max(longest_substring, len(unique_chars))
                break
            else:
                unique_chars[to_char] = j

        # After last run choose max again
        longest_substring = max(longest_substring, len(unique_chars))

    return longest_substring


def test_length_longest_substring():
    assert length_longest_substring("") == 0
    assert length_longest_substring("u") == 1
    assert length_longest_substring("bbbbb") == 1
    assert length_longest_substring("abcabcbb") == 3
