def find_index(needle, haystack):
    if needle == "" or haystack == "":
        return -1

    # Very primitive approach
    for first_idx in range(0, len(haystack) - len(needle) + 1):
        last_idx = first_idx + len(needle)
        if needle == haystack[first_idx:last_idx]:
            return first_idx

    return -1

assert find_index("", "bbab") == -1
assert find_index("", "") == -1
assert find_index("a", "") == -1

assert find_index("a", "bbab") == 2
assert find_index("a", "baba") == 1
assert find_index("a", "bbba") == 3
assert find_index("baba", "babaab") == 0
