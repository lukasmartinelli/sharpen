class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode {}>'.format(self.val)


def level_order(root):

    def level_order_nodes():
        levels = [[root]]

        while True:
            next_level = []
            for node in levels[-1]:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if len(next_level) > 0:
                levels.append(next_level)
            else:
                break

        return levels

    # Transform nodes to ints
    # TODO: This shouldn't be necessary
    levels = level_order_nodes()
    for level in levels:
        for idx, node in enumerate(level):
            level[idx] = node.val

    return levels


def test_level_order():
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

    assert level_order(root) == [
        [4],
        [2, 6],
        [1, 3, 5],
    ]
