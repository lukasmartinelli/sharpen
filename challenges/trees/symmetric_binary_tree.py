"""
Given a binary tree, check whether it
is a mirror of itself(symmetric around its center)


Symmetric binary tree.

        1
       / \
      2   2
     / \ / \
    3  4 4  3

Not symmetric binary tree.

        1
       / \
      2   2
       \   \
       3    3
"""


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode {}>'.format(self.val)


def is_symmetric(root):

    def compare_nodes(n1, n2):
        if n1 is None or n2 is None:
            return n1 == n2
        elif n1.left  != n2.right:
            return False
        else:
            return compare_nodes(n1.left, n2.right) and compare_nodes(n1.right, n2.left)

    return root is None or compare_nodes(root.left, root.right)
