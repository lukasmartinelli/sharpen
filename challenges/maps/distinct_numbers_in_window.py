class DistinctDict():
    def __init__(self, start=[]):
        self.uniques = {}

    def add(self, num):
        print('Add', num)
        if num in self.uniques:
            self.uniques[num] = self.uniques[num] + 1
        else:
            self.uniques[num] = 1

    def remove(self, num):
        print('Remove', num)
        count = self.uniques[num]

        if count > 1:
            self.uniques[num] = count - 1
        else:
            del self.uniques[num]

    def distinct_numbers(self):
        print('Distincts', self.uniques)
        return len(self.uniques)


def distinct_numbers_in_windows(numbers, k):
    if k == 0 or k > len(numbers):
        return

    distinct_dict = DistinctDict(numbers[:k])

    for i, num in enumerate(numbers):
        if i < k - 1:
            distinct_dict.add(num)
        elif i == k - 1:
            distinct_dict.add(num)
            yield distinct_dict.distinct_numbers()
        else:
            oldest_num = numbers[i - k]
            distinct_dict.remove(oldest_num)
            distinct_dict.add(num)
            yield distinct_dict.distinct_numbers()


def test_d_nums():
    nums = [1, 2, 1, 3, 4, 3]
    assert list(distinct_numbers_in_windows(nums, k=3)) == [2, 3, 3, 2]
    nums = [6, 3, 2, 2, 4, 3, 6, 3, 1, 2, 3]
    assert list(distinct_numbers_in_windows(nums, k=4)) == [3, 3, 3, 4, 3, 3, 4, 3]
