import math


def find_single_number(arr):
    single_number = 0

    for num in arr:
        mask = 1 << num
        single_number ^= mask

    return int(math.log(single_number, 2))


assert find_single_number([1, 2, 2, 3, 1]) == 3
