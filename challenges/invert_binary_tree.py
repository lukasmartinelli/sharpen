class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode {}>'.format(self.val)


def invert_tree(n):
    if n is None:
        return

    tmp = n.left
    n.left = n.right
    n.right = tmp

    invert_tree(n.left)
    invert_tree(n.right)

    return n


def test_invert_tree():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)

    n1.left = n2
    n1.right = n3

    n2.left = n4
    n2.right = n5

    n3.left = n6
    n3.right = n7

    root = invert_tree(n1)

    assert root == n1
    assert root.left == n3
    assert root.right == n2

    assert n3.left == n7
    assert n3.right == n6

    assert n2.left == n5
    assert n2.right == n4
