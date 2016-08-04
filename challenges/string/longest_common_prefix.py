def longest_common_prefix(strs):
    if len(strs) < 1:
        return ''

    def find_prefix():
        for idx in range(0, len(strs[0])):
            expected_char = strs[0][idx]

            for str in strs[1:]:
                if len(str) <= idx or str[idx] != expected_char:
                    return

            yield expected_char

    return ''.join(find_prefix())


def test_prefix():
    assert longest_common_prefix([]) == ''
    assert longest_common_prefix(['a', 'b', 'c']) == ''
    assert longest_common_prefix(['abcd', 'abcd', 'aba']) == 'ab'
