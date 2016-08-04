class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode {}>'.format(self.val)


def sum_root_leaf_paths(root):
    paths = root_leaf_paths(root, [])

    def number_from_path(p):
        digits = [str(node.val) for node in p]
        return int(''.join(digits))

    numbers = [number_from_path(p) for p in paths]
    return sum(numbers) % 1003


def root_leaf_paths(node, path):
    if node is None:
        return

    if node.left is None and node.right is None:
        yield path + [node]

    for p in root_leaf_paths(node.left, path + [node]):
        yield p

    for p in root_leaf_paths(node.right, path + [node]):
        yield p


def test_sum_root_leaf_paths():
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

    assert sum_root_leaf_paths(root) == 306


def test_sum_root_leaf_paths_single_node():
    assert sum_root_leaf_paths(TreeNode(3)) == 3
