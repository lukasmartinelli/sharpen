class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return 'Node<{},{}>'.format(self.val, self.next)


def swap_nodes_in_pairs(head):
    # Keep new head around to return it at last
    if head.next:
        new_head = head.next
    else:
        return head

    while head is not None:
        first_node = head
        second_node = first_node.next
        third_node = second_node.next if second_node else None
        forth_node = third_node.next if third_node else None

        if second_node:
            second_node.next = first_node

        if forth_node:
            first_node.next = forth_node
        else:
            first_node.next = third_node

        head = third_node

    return new_head


def test_one_node_swap():
    a1 = ListNode(1)
    assert swap_nodes_in_pairs(a1) == a1


def test_swap():
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)
    a5 = ListNode(5)
    a6 = ListNode(6)

    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a5.next = a6

    swapped_head = swap_nodes_in_pairs(a1)
    assert swapped_head == a2

    swapped_head = swapped_head.next
    assert swapped_head == a1

    swapped_head = swapped_head.next
    assert swapped_head == a4

    swapped_head = swapped_head.next
    assert swapped_head == a3

    swapped_head = swapped_head.next
    assert swapped_head == a6

    swapped_head = swapped_head.next
    assert swapped_head == a5


def test_uneven_swap():
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)
    a5 = ListNode(5)

    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5

    swapped_head = swap_nodes_in_pairs(a1)
    assert swapped_head == a2

    swapped_head = swapped_head.next
    assert swapped_head == a1

    swapped_head = swapped_head.next
    assert swapped_head == a4

    swapped_head = swapped_head.next
    assert swapped_head == a3

    swapped_head = swapped_head.next
    assert swapped_head == a5


def test_uneven_small_swap():
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)

    a1.next = a2
    a2.next = a3

    swapped_head = swap_nodes_in_pairs(a1)
    assert swapped_head == a2
    swapped_head = swapped_head.next
    assert swapped_head == a1
    swapped_head = swapped_head.next
    assert swapped_head == a3
