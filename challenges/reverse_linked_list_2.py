class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return '<Node {} {}>'.format(self.val, self.next)


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


n1 = ListNode(0)
n2 = ListNode(1)
n3 = ListNode(2)
n4 = ListNode(3)

n1.next = n2
n2.next = n3
n3.next = n4

linked_list = n1
print(reverse_linked_list(linked_list))
