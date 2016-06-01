

def compare_version(version1, version2):
    """
    Compare version strings are non-empty and contain only digits
    and the . character.

    Example of ordering:
    0.1 < 1.1 < 1.2 < 1.13 < 1.13.4
    """

    def revisions(v):
        if len(v.strip()) == 0:
            return [0]

        return [int(digits) for digits in v.split('.')]

    def ensure_revision_length(r, length):
        return r + (length - len(r)) * [0]

    revisions1 = revisions(version1)
    revisions2 = revisions(version2)

    max_len = max(len(revisions1), len(revisions2))
    revisions1 = ensure_revision_length(revisions1, max_len)
    revisions2 = ensure_revision_length(revisions2, max_len)

    for r1, r2 in zip(revisions1, revisions2):
        if r1 > r2:
            return 1
        elif r1 < r2:
            return -1

    return 0


assert compare_version('1', '1.0') == 0
assert compare_version('1', '') == 1
assert compare_version('1', '1') == 0
assert compare_version('1.1', '1') == 1
assert compare_version('0.1', '1.1') == -1
assert compare_version('1.13', '1.13.4') == -1
assert compare_version('2.5', '2.5.1') == -1
