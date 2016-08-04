"""
Given an array A, count the number of inversions in the array.
Formally speaking, two elements A[i] and A[j]
form an inversion if A[i] > A[j] and i < j
"""


class TreeNode():
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode {}, {}>'.format(self.val, self.idx)

    def insert(self, num, idx):
        if num < self.val:
            if not self.left:
                self.left = TreeNode(num, idx)
            else:
                self.left.insert(num, idx)
        else:
            if not self.right:
                self.right = TreeNode(num, idx)
            else:
                self.right.insert(num, idx)


def find_lower(node, num):
    if not node:
        return

    if node.val > num:
        for n in find_lower(node.left, num):
            yield n
    else:
        yield node

        for n in find_lower(node.left, num):
            yield n
        for n in find_lower(node.right, num):
            yield n


def prepare_bin_tree(numbers):
    root = TreeNode(numbers[0], 0)
    for idx, num in enumerate(numbers[1:], start=1):
        root.insert(num, idx)

    return root


def inversions(numbers):
    # O(n * log n)
    tree = prepare_bin_tree(numbers)

    for idx, num in enumerate(numbers):
        for node in find_lower(tree, num):
            if node.idx > idx and node.val < num:
                yield num, node.val


def test_insert():
    nums = [2, 4, 1, 3, 5]
    tree = prepare_bin_tree(nums)

    assert tree.val == 2
    assert tree.left.val == 1
    assert tree.right.val == 4
    assert tree.right.left.val == 3
    assert tree.right.right.val == 5


def test_inversions():
    nums = [2, 4, 1, 3, 5]
    assert list(inversions(nums)) == [(2, 1), (4, 1), (4, 3)]
