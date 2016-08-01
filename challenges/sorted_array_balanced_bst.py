class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode {}>'.format(self.val)


def sorted_array_to_bst(arr):
    if len(arr) == 0:
        return None

    mid = len(arr) / 2
    node = TreeNode(arr[mid])
    node.left = sorted_array_to_bst(arr[:mid])
    node.right = sorted_array_to_bst(arr[mid+1:])

    return node


def test_uneven_bst():
    nums = [1, 2, 3]
    bst = sorted_array_to_bst(nums)

    assert bst.val == 2
    assert bst.left.val == 1
    assert bst.right.val == 3


def test_is_bst():
    nums = [1, 2, 3, 4, 5, 6]
    bst = sorted_array_to_bst(nums)

    assert bst.val == 4

    n2 = bst.left
    n6 = bst.right

    assert n2.val == 2
    assert n2.left.val == 1
    assert n2.right.val == 3

    assert n6.val == 6
    assert n6.left.val == 5
    assert n6.right is None


def test_single_node_bst():
    nums = [1]
    bst = sorted_array_to_bst(nums)
    assert bst.val == 1
