class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode {}>'.format(self.val)


def min_depth(node, depth=1):
    if node.left is None and node.right is None:
        return depth

    if node.left is None:
        return min_depth(node.right, depth+1)

    if node.right is None:
        return min_depth(node.left, depth+1)

    return min(
        min_depth(node.left, depth+1),
        min_depth(node.right, depth+1)
    )


def create_test_tree():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)

    n4.left = n2
    n4.right = n6

    n2.left = n1
    n2.right = n3

    n6.left = n5

    root = n4

    return root


def test_min_depth():
    root = create_test_tree()
    assert min_depth(root) == 3


def test_min_depth_no_left_side():
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n2.right = n3
    root = n2

    assert min_depth(root) == 2


def test_min_depth_leaf_node():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n1.left = n2
    n2.right = n3
    root = n1

    assert min_depth(root) == 3
