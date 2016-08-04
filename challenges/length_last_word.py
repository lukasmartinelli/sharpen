def length_last_word(s):
    """
    Given a string s consists of upper/lower-case alphabets and
    empty space characters ' ', return the length of last word in the string.
    """
    s = s.strip()
    word_length = 0
    for c in s:
        if c == ' ':
            word_length = 0
        else:
            word_length += 1
    return word_length


def test_length_last_word():
    assert length_last_word('Hey man whats up') == 2
    assert length_last_word('Yo') == 2
    assert length_last_word('Yo yo man ') == 3
    assert length_last_word('') == 0
