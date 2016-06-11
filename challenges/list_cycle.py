class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '<Node {} {}>'.format(self.val, self.next)


class LinkedList(ListNode):
    def __init__(self, arr):

        nodes = [ListNode(v) for v in arr]
        for i in range(1, len(nodes)):
            nodes[i-1].next = nodes[i]

        head = nodes[0]

        self.val = head.val
        self.next = head.next


def detect_cycle(head):
    node_lookup = {}

    cursor = head
    while cursor:
        if id(cursor.next) in node_lookup:
            return cursor.next

        node_lookup[id(cursor)] = cursor
        cursor = cursor.next

    print(len(node_lookup))

    return None


def test_small_cycle():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n3  # introduce loop

    assert detect_cycle(n1) == n3


def test_no_cycle():
    large_list = LinkedList(range(0, 100000))
    assert detect_cycle(large_list) is None
