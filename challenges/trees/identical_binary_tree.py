class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode {}>'.format(self.val)

    def __eq__(self, other):
        return eq_node(self, other)


def is_same_tree(tree_a, tree_b):
    "Given two binary trees ensure they have the same nodes."
    return compare_recursive(tree_a, tree_b)


def compare_recursive(a, b):
    if not a and not b:
        return True

    if a and not b:
        return False

    if not a and b:
        return False

    if a.val != b.val:
        return False

    return compare_recursive(a.left, b.left) and compare_recursive(a.right, b.right)


def test_is_same_tree():
    def create_tree():
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)

        n1.left = n2
        n1.right = n3
        return n1

    assert is_same_tree(create_tree(), create_tree())


def test_is_not_same_tree():
    def create_tree_1():
        n1 = TreeNode(1)
        n3 = TreeNode(3)

        n1.right = n3
        return n1

    def create_tree_2():
        n1 = TreeNode(1)
        n2 = TreeNode(2)

        n1.left = n2
        return n1

    assert not is_same_tree(create_tree_1(), create_tree_2())
