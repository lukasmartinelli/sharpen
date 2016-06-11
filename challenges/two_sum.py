def two_sum(numbers, target):
    lookup = {}
    for idx, num in enumerate(numbers, start=1):
        needed_summand = target - num
        # print('Num {} -> need summand {}'.format(num, needed_summand), lookup)

        if needed_summand in lookup:
            return [lookup[needed_summand], idx]
        elif num not in lookup:
            lookup[num] = idx

    return []


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum([2, 7, 11, 15], 7) == []
    assert two_sum([2, 7, 11, 15], 8) == []
    assert two_sum([2, 7, 11, 15], 17) == [1, 4]


def test_two_sum_multiple_possiblities():
    assert two_sum([1, 7, 8, 2], 9) == [1, 3]

def test_two_sum_negative():
    nums = [4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7,
            7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7,
            7, 9, -4, 4, -8]

    assert two_sum(nums, -3) == [4, 8]
