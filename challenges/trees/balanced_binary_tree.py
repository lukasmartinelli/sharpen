class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode {}>'.format(self.val)


def is_leaf(node):
    return node.left is None and node.right is None


def tree_height(node):
    if node is None:
        return 0
    elif is_leaf(node):
        return 1
    else:
        left_height = tree_height(node.left)
        right_height = tree_height(node.right)
        return max(left_height, right_height) + 1


def is_balanced(root):
    if root is None:
        return True

    left_height = tree_height(root.left)
    right_height = tree_height(root.right)

    balanced = abs(left_height - right_height) <= 1
    print(balanced, left_height, right_height, root)
    return balanced and is_balanced(root.left) and is_balanced(root.right)


def test_is_balanced():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n1.left = n2
    n1.right = n3

    assert is_balanced(n1)


def test_is_not_balanced():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n3.left = n2
    n2.left = n1

    assert not is_balanced(n3)


def test_single_node_tree_is_balanced():
    n1 = TreeNode(1)
    assert is_balanced(n1)


def test_two_node_tree_is_balanced():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n1.right = n2
    assert is_balanced(n1)


def test_equal_height_of_root_is_inbalanced():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n4 = TreeNode(4)
    n5 = TreeNode(5)

    n1.left = n2
    n1.right = n4

    n4.right = n5

    assert is_balanced(n1)
