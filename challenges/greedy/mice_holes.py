def assign_mice_to_holes(mice, holes):
    """
    There are N mice and N holes are placed in a straight line.
    Each hole can accomodate only 1 mouse.
    A mouse can stay at his position, move one step right from x to x + 1,
    or move one step left from x to x - 1. Any of these moves
    consumes 1 minute.
    Assign mice to holes so that the time when the last mouse gets inside
    a hole is minimized.
    """
    mice = sorted(mice)
    holes = sorted(holes)

    max_time = 0

    for m, h in zip(mice, holes):
        max_time = max(max_time, abs(m - h))

    return max_time


def test_assign_mices_to_holes():
    assert assign_mice_to_holes([4, -4, 2], [4, 0, 5]) == 4
    assert assign_mice_to_holes([-4, 2, 4], [-20, -18, -19]) == 22
    assert assign_mice_to_holes([
        35, 72, -95, -54, 89, 5, 23, 13, 38, 20, 66,
        26, 63, 44, -50, -23, -85, -72, -47, -96
    ], [
        24, 45, -36, 26, -43, 80, -45, 19, -93, -92, -70,
        -54, -63, -9, -62, 36, 96, -68, -75, -57
    ]) == 63
