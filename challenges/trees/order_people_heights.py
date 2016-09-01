def order_people_heights(heights, in_fronts):
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


def verify_infronts(people):
    for i, (height, in_front) in enumerate(people):
        taller_people_in_front = 0
        for previous_height, _ in people[:i]:
            if previous_height > height:
                taller_people_in_front += 1

        if taller_people_in_front != in_front:
            return False

    return True


def permutations(permutation, items):
    if len(items) == 0:
        yield permutation
        return

    for i, n in enumerate(items):
        next_permutation = permutation + [n]
        remaining_path = items[:i] + items[i+1:]
        for p in permutations(next_permutation, remaining_path):
            yield p


def test_order_people_heights():
    heights = [5, 3, 2, 6, 1, 4]
    in_fronts = [0, 1, 2, 0, 3, 2]
    assert order_people_heights(heights, in_fronts) == [5, 3, 2, 1, 6, 4]


def test_permutations():
    items = [1, 2, 3]
    assert list(permutations([], items)) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


def test_verify_infronts():
    people1 = [(5, 0), (3, 1), (2, 2), (6, 0), (1, 3), (4, 2)]
    assert not verify_infronts(people1)

    people2 = [(5, 0), (3, 1), (2, 2), (1, 3), (6, 0), (4, 2)]
    assert verify_infronts(people2)
