def permute(numbers):

    def all_permutations(nums):
        if len(nums) == 1:
            yield nums

        previous_nums = {}
        for idx, num in enumerate(nums):
            if num not in previous_nums:
                previous_nums[num] = True
                copy = list(nums)
                copy.pop(idx)

                for permutations in all_permutations(copy):
                    yield [num] + permutations

    return list(all_permutations(numbers))


def test_permutations():
    assert permute([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]


def test_permutations_with_duplicates():
    assert permute([1, 1, 3]) == [
        [1, 1, 3],
        [1, 3, 1],
        [3, 1, 1],
    ]
