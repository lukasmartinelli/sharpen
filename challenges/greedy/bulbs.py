def switch_bulbs_on(bulbs):
    """
    N light bulbs are connected by a wire. Each bulb has a switch
    associated with it, however due to faulty wiring, a switch also
    changes the state of all the bulbs to the right of current bulb.

    Given an initial state of all bulbs, find the minimum number of switches
    you have to press to turn on all the bulbs. You can press the same
    switch multiple times.
    """
    min_switch_changes = 0
    flipped = False

    for b in bulbs:
        if (b == 0 and not flipped) or (b == 1 and flipped):
            flipped = not flipped
            min_switch_changes += 1
    return min_switch_changes


def test_switch_bulbs_on():
    assert switch_bulbs_on([0, 1, 0, 1]) == 4
    assert switch_bulbs_on([0, 0, 0, 0]) == 1
    assert switch_bulbs_on([0, 1, 0, 0]) == 3
