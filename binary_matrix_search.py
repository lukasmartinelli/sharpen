class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        pass


def binary_search_exists(numbers, num):
    "O(log n) where n is len(numbers)"
    first = 0
    last = len(numbers) - 1

    while first <= last:
        mid = (first + last) / 2
        if numbers[mid] == num:
            return True
        if numbers[mid] < num:
            first = mid + 1
        if numbers[mid] > num:
            last = mid - 1

    return False


def binary_search_matrix(matrix, num):
    if len(matrix) == 0:
        return False

    first = 0
    last = len(matrix) - 1

    while first <= last:
        mid = (first + last) / 2

        if matrix[mid][0] <= num <= matrix[mid][-1]:
            return binary_search_exists(matrix[mid], num)

        if matrix[mid][0] < num > matrix[mid][-1]:
            first = mid + 1

        if matrix[mid][0] > num:
            last = mid - 1

    return False

    

print(binary_search_exists([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
print(binary_search_exists([1, 2, 3, 4, 5, 6, 7, 8, 9], 7))

print(binary_search_matrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 23))
print(binary_search_matrix([
  [1],
  [10],
  [23]
], 1))
print(binary_search_matrix([
  [1]
], 1))
print(binary_search_matrix([
  [1,   3,  5,  7]
], 5))
