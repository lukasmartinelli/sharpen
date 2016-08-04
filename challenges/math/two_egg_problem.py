"""
A building has 100 floors. One of the floors is the highest floor an
egg can be dropped from without breaking.

If an egg is dropped from above that floor, it will break.
If it is dropped from that floor or below, it will be completely
undamaged and you can drop the egg again.

Given two eggs, find the highest floor an egg can be dropped from
without breaking, with as few drops as possible.
"""

class Floor(object):
    def __init__(self, floor_number, breaks=False):
        self.floor_number = floor_number
        self.breaks = breaks

    def __repr__(self):
        return '<Floor {},{}>'.format(self.floor_number, self.breaks)


def building(floors=100, breaking_floor=56):
    def make_floor(i):
        return Floor(i, breaks=i >= breaking_floor)

    return [make_floor(i) for i in range(1, 101)]


def find_highest_floor(floors):

    # Since we must find a solution we always need the 'backup' egg to
    # solve the problem in worst time
    def ascending_drop_egg_until_breaks(start_idx):
        for i in range(start_idx, len(floors)):
            if floors[i].breaks:
                return i

    # This frees us up to do probing with the first egg
    def drop_egg_until_breaks(previous_guess):
        guess = previous_guess + (previous_guess / 2)
        "Use binary search until first egg breaks"
        print('Check if egg breaks at floor {}'.format(guess))

        if floors[guess].breaks:
            return previous_guess
        else:
            return drop_egg_until_breaks(guess)

    half = len(floors) / 2
    if floors[half].breaks:
        return ascending_drop_egg_until_breaks(0)

    first_breaking_floor = drop_egg_until_breaks(half)
    print('Egg breaks at floor {}'.format(first_breaking_floor))

    return ascending_drop_egg_until_breaks(first_breaking_floor)


def test_find_highest_floor():
    building1 = building(breaking_floor=54)
    assert find_highest_floor(building1) == 53

    building2 = building(breaking_floor=25)
    assert find_highest_floor(building2) == 24

    building3 = building(breaking_floor=100)
    assert find_highest_floor(building3) == 99
