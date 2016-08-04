class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode {}>'.format(self.val)


def max_depth(node, depth=0):
    if node is None:
        return depth

    return max(
        max_depth(node.left, depth+1),
        max_depth(node.right, depth+1)
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


def test_postorder_larger_tree():
    root = create_test_tree()
    assert max_depth(root) == 3
