class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return self.val == other.val and self.next == other.next

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


def reverse_sublist(succeeding_tail, sublist_len):
    if succeeding_tail.next:
        sublist_head, sublist_tail, rest = reverse_linked_list(succeeding_tail.next, sublist_len)

        # Relink the reversed sublist if
        succeeding_tail.next = sublist_head
        sublist_tail.next = rest


def reverse_linked_list_positional(head, m, n):
    """
    Reverse a linked list from position m to n.
    """
    cursor = head

    if m == 1:
        dummy = ListNode("Dummy")
        dummy.next = cursor
        reverse_sublist(dummy, n + 1 - m)
        return dummy.next

    pos = 1
    while cursor:
        pos += 1
        if pos < m:
            cursor = cursor.next
        else:
            break

    reverse_sublist(cursor, n + 1 - m)

    return head


def reverse_linked_list(head, max_node_count):
    """
    Reverse linked list but only up to max_node_count.
    Return the new head and tail of the linked list.
    """
    if not head:
        return None, None, None

    count = 1
    first_node = head
    second_node = head.next
    head.next = None  # Make sure list has no cycle

    while second_node and count < max_node_count:
        third_node = second_node.next
        second_node.next = first_node

        first_node = second_node
        second_node = third_node

        count += 1

    rest = second_node
    tail = head  # Old head is the new tail
    head = first_node  # Head is now the last node

    return head, tail, rest


def test_reverse_linked_list():
    a = LinkedList([5, 4, 3, 2, 1])
    head, tail, rest = reverse_linked_list(a, 5)
    assert head == LinkedList([1, 2, 3, 4, 5])
    assert tail == ListNode(5)
    assert rest is None


def test_reverse_linked_list_partially():
    a = LinkedList([7, 6, 5, 4, 3, 2, 1])
    head, tail, rest = reverse_linked_list(a, 4)
    assert head == LinkedList([4, 5, 6, 7])
    assert tail == ListNode(7)
    assert rest == LinkedList([3, 2, 1])


def test_reverse_linked_list_positional():
    a = LinkedList([1, 2, 3, 4, 5])
    head = reverse_linked_list_positional(a, m=2, n=4)
    assert head == LinkedList([1, 4, 3, 2, 5])


def test_reverse_linked_list_short():
    a = LinkedList([1])
    head = reverse_linked_list_positional(a, m=1, n=1)
    assert head == LinkedList([1])

    b = LinkedList([1, 2])
    head = reverse_linked_list_positional(b, m=1, n=2)
    assert head == LinkedList([2, 1])
