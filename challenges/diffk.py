def diff_possible(numbers, k):
    """
    Given a list of sorted integers and a non negative
    integer k, find if there exists 2 indicies i and j
    such that A[i] - A[j] = k, i != j
    """
    if k < 0:
        raise ValueError('k can not be non negative')

    # Find k since as long as i is not larger than k
    # we do not even need to compare
    if numbers[-1] < k:
        return False

    start_i = 0
    while start_i < len(numbers):
        if numbers[start_i] >= k:
            break
        else:
            start_i += 1

    for i in range(start_i, len(numbers)):
            needed_num = numbers[i] - k
            for j in reversed(range(0, i)):
                if numbers[j] == needed_num:
                    return True
                elif numbers[j] < needed_num:
                    # All hope is lost, we can never reach k again
                    break
    return False


assert diff_possible([0, 1, 1, 5, 6, 7, 8, 12, 22], 10)
assert diff_possible([1, 3, 5], 4)
assert not diff_possible([1, 3, 5], 3)
assert diff_possible([1, 2, 10, 15], 5)
assert not diff_possible([1, 2, 2], 5)
