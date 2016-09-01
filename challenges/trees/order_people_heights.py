

def order_people_heights(heights, in_fronts):
    """
    You are given a list of people. Each person has a height and how many
    before it are taller.

        heights =         [5, 3, 2, 6, 1, 4]
        people_in_front = [0, 1, 2, 0, 3, 2]

    And this is what it look like

                 x
        x        x
        x        x     x
        x  x     x     x
        x  x  x  x     x
        x  x  x  x  x  x

        0  1  2  0  3  2

    Order people heights that they fulfill their people in front constraint.

        ordered_heights =  [5, 3, 2, 6, 1, 4]

                    x
        x           x
        x           x  x
        x  x        x  x
        x  x  x     x  x
        x  x  x  x  x  x

        0  1  2  3  0  2

    """
    people = sorted(zip(heights, in_fronts), key=lambda p: p[0])
    ordered_people = [None] * len(people)

    for height, in_front in people:
        if people[in_front] is None:
            people[in_front] = height
        else:
            empty_slots = [i for i, h in enumerate(ordered_people) if h is None]
            i = empty_slots[in_front]
            ordered_people[i] = height

    return ordered_people


def test_order_people_heights():
    heights = [5, 3, 2, 6, 1, 4]
    in_fronts = [0, 1, 2, 0, 3, 2]
    assert order_people_heights(heights, in_fronts) == [5, 3, 2, 1, 6, 4]
