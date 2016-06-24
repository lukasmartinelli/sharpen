class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode {}>'.format(self.val)


def inorder(node):
    if not node:
        return

    for n in inorder(node.left):
        yield n

    yield node

    for n in inorder(node.right):
        yield n


def subtree_greater(node, val):
    nodes = [n.val for n in inorder(node)]
    if len(nodes) > 0:
        return min(nodes) > val

    return True


def subtree_lesser(node, val):
    nodes = [n.val for n in inorder(node)]
    if len(nodes) > 0:
        return max(nodes) < val

    return True


def is_valid_bst(node):
    if not node:
        return True

    valid = subtree_lesser(node.left, node.val) and subtree_greater(node.right, node.val)
    return valid and is_valid_bst(node.left) and is_valid_bst(node.right)


def test_is_invalid_bst():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)

    n2.left = n1
    n2.right = n3
    n3.left = n4

    assert not is_valid_bst(n2)


def test_is_valid_bst():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)

    n2.left = n1
    n2.right = n3
    n3.right = n4

    assert is_valid_bst(n2)
