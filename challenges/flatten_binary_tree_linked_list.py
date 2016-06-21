class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode {}>'.format(self.val)


def flatten(root):
    n = root
    while True:
        if n.left is not None:
            last_leaf = find_last_leaf(n.left)
            last_leaf.right = n.right

            n.right = n.left
            n.left = None

            n = n.right
        elif n.right is not None:
            n = n.right
        else:
            break

    return root


def find_last_leaf(n):
    if n.right is not None:
        return find_last_leaf(n.right)
    elif n.left is not None:
        return find_last_leaf(n.left)
    else:
        return n


def test_flatten_left_side_tree():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n1.left = n2
    n2.left = n3

    n1 = flatten(n1)

    assert n1.left is None and n1.right == n2
    assert n2.left is None and n2.right == n3
    assert n3.left is None and n3.right is None


def test_flatten_tree():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)

    n1.left = n2
    n1.right = n5

    n2.left = n3
    n2.right = n4

    n5.right = n6

    n1 = flatten(n1)

    assert n1.left is None
    assert n1.right == n2

    assert n2.right == n3
    assert n2.left is None

    assert n3.left is None
    assert n3.right == n4

    assert n4.left is None
    assert n4.right == n5

    assert n5.left is None
    assert n5.right == n6

    assert n6.left is None and n6.right is None



def test_find_last_leaf():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)

    n1.left = n2
    n1.right = n4

    n2.right = n3

    assert find_last_leaf(n1) == n4
    assert find_last_leaf(n2) == n3
