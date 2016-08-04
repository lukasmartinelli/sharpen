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


def kth_smallest(root, k):
    for pos, node in enumerate(inorder(root), start=1):
        if pos == k:
            return node

    return None


def test_kth_smallest():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n2.left = n1
    n2.right = n3

    root = n2
    assert kth_smallest(root, k=1) == n1
    assert kth_smallest(root, k=2) == n2
    assert kth_smallest(root, k=3) == n3
