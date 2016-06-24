import collections


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '<TreeNode {}>'.format(self.val)


def inorder_level(node, level=0):
    if not node:
        return

    for rslt in inorder_level(node.left, level=level+1):
        yield rslt

    yield level, node

    for rslt in inorder_level(node.right, level=level+1):
        yield rslt


def zigzag():
    yield True
    yield False


def zigzag_level_order(root):
    levels = collections.defaultdict(collections.deque)

    for level, node in inorder_level(root):
        if level % 2 == 0:
            levels[level].append(node.val)
        else:
            levels[level].appendleft(node.val)

    for key in levels.keys():
        levels[key] = list(levels[key])

    return levels.values()


def test_zigzag_level_order():
    n3 = TreeNode(3)
    n9 = TreeNode(9)
    n20 = TreeNode(20)
    n15 = TreeNode(15)
    n7 = TreeNode(7)

    n3.left = n9
    n3.right = n20
    n20.left = n15
    n20.right = n7

    root = n3
    assert zigzag_level_order(root) == [[3], [20, 9], [15, 7]]
