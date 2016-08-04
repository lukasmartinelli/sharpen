class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode {}>'.format(self.val)


def path_sum(root, target_sum):
    """
    Given a binary tree and a sum, determine if the tree has
    a root-to-leaf path such that adding up all the values along
    the path equals the given sum.
    """

    def is_leaf(node):
        return node.left is None and node.right is None

    def leaf_nodes(node, parent_path_sum):
        if node is None:
            return

        new_sum = parent_path_sum + node.val
        if is_leaf(node):
            yield (node, new_sum)

        for n in leaf_nodes(node.left, new_sum):
            yield n

        for n in leaf_nodes(node.right, new_sum):
            yield n

    for node, path_sum in leaf_nodes(root, 0):
        if path_sum == target_sum:
            return True

    return False


def test_invert_tree():
    n1 = TreeNode(5)
    n2 = TreeNode(4)
    n3 = TreeNode(8)
    n4 = TreeNode(11)
    n5 = TreeNode(7)
    n6 = TreeNode(2)
    n7 = TreeNode(13)
    n8 = TreeNode(4)
    n9 = TreeNode(1)

    n1.left = n2
    n1.right = n3

    n2.left = n4
    n4.left = n5
    n4.right = n6

    n3.left = n7
    n3.right = n8
    n8.right = n9

    assert path_sum(n1, 22)
