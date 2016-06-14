class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode {}>'.format(self.val)


def inorder2(node):
    nodes = []

    cursor = node
    nodes.append(cursor)

    if cursor.left is None:
        yield cursor

    if cursor.right:
        yield cursor.ri
    node.left


def inorder(root):

    def inorder_recursive(node):
        if not node:
            return

        for n in inorder_recursive(node.left):
            yield n

        yield node

        for n in inorder_recursive(node.right):
            yield n

    return [n.val for n in inorder_recursive(root)]


def test_inorder():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n1.left = n2
    n1.right = n3

    assert inorder(n1) == [2, 1, 3]


def test_inorder_imbalanced():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n1.right = n2
    n2.left = n3

    assert inorder(n1) == [1, 3, 2]


def test_inorder_larger_tree():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)

    n4.left = n2
    n4.right = n6

    n2.left = n1
    n2.right = n3

    n6.left = n5
    n6.right = n7

    root = n4
    assert inorder(root) == [1, 2, 3, 4, 5, 6, 7]
