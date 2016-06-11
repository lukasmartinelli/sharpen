def permute(numbers):
    numbers = set(numbers)
    def recursive_permutations(path):
        if len(path) == len(numbers):
            yield path

        remaining_choices = [num for num in numbers if num not in path]
        for num in remaining_choices:
            new_path = path + [num]
            for permuted_path in recursive_permutations(new_path):
                yield permuted_path

    return list(recursive_permutations([]))


def test_permutations():
    assert permute([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ]
