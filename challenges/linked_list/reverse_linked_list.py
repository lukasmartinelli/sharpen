class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '<Node {} {}>'.format(self.val, self.next)

    def values(self):
        cursor = self
        while cursor is not None:
            yield cursor.val
            cursor = cursor.next


def reverse_linked_list(head):
    prev = head
    cur = head.next
    head.next = None

    while cur is not None:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp

    return prev


def test_reverse_linked_list():
    n1 = ListNode(0)
    n2 = ListNode(1)
    n3 = ListNode(2)
    n4 = ListNode(3)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    linked_list = n1
    reversed_list = reverse_linked_list(linked_list)

    assert list(reversed_list.values()) == [3, 2, 1, 0]
