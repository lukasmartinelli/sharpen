"""
Find the lowest common ancestor in an unordered binary tree given two
values in the tree.

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2_     0        8
         /   \
         7    4

For the above tree, the least common ancestor of nodes 5 and 0 is 3.
"""


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode {}>'.format(self.val)


def least_common_ancestor(root, a, b):
    # find a in O(log n)
    # find b in O(log n)
    # compare paths of a and b to find a common ancestor
    # this works because there are no duplicates

    path_a = find_path(root, a, [])
    path_b = find_path(root, b, [])
    return find_least_common_ancestor_in_paths(path_a, path_b)


def find_path(node, val, previous_path):
    if node is None:
        return []

    if node.val == val:
        return previous_path + [node.val]

    left_path = find_path(node.left, val, previous_path + [node.val])
    if len(left_path) > 0:
        return left_path

    right_path = find_path(node.right, val, previous_path + [node.val])
    if len(right_path) > 0:
        return right_path

    return []


def find_least_common_ancestor_in_paths(path_a, path_b):
    # 2 * O(n)
    lookup = set(path_a)

    # O(n) * O(1)
    for val in reversed(path_b):
        if val in lookup:
            return val

    return None


def create_test_tree():
    n3 = TreeNode(3)

    n5 = TreeNode(5)
    n3.left = n5
    n5.left = TreeNode(6)

    n2 = TreeNode(2)
    n5.right = n2
    n2.left = TreeNode(7)
    n2.right = TreeNode(4)

    n1 = TreeNode(1)
    n3.right = n1

    n1.left = TreeNode(0)
    n1.right = TreeNode(8)

    return n3


def test_find_path():
    root = create_test_tree()
    assert find_path(root, 5, []) == [3, 5]
    assert find_path(root, 7, []) == [3, 5, 2, 7]
    assert find_path(root, 0, []) == [3, 1, 0]
    assert find_path(root, 10, []) == []


def test_find_least_common_ancestor_in_paths():
    assert find_least_common_ancestor_in_paths([3, 4, 1, 2], [3, 4]) == 4
    assert find_least_common_ancestor_in_paths([3, 1, 0, 8], [3, 5, 2, 4]) == 3
    assert find_least_common_ancestor_in_paths([3, 5, 2, 4], [3, 5, 6]) == 5


def test_find_least_common_ancestor():
    root = create_test_tree()
    assert least_common_ancestor(root, 5, 1) == 3
    assert least_common_ancestor(root, 5, 4) == 5
    assert least_common_ancestor(root, 2, 0) == 3
    assert least_common_ancestor(root, 7, 4) == 2
