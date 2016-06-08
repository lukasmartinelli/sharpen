class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return 'Node<{},{}>'.format(self.val, self.next)


def linked_list_len(head):
    length = 0
    while head is not None:
        length += 1
        head = head.next
    return length


def fast_forward_linked_list(head, offset):
    for _ in xrange(0, offset):
        head = head.next

    return head


def fast_forward_larger_list(list_a, list_b):
    len_a = linked_list_len(list_a)
    len_b = linked_list_len(list_b)

    min_length = min(len_a, len_b)
    offset = abs(len_a - len_b)

    if len_a > len_b:
        list_a = fast_forward_linked_list(list_a, offset)
    elif len_b > len_a:
        list_b = fast_forward_linked_list(list_b, offset)

    return min_length, list_a, list_b


def find_intersection_node(list_a, list_b):
    min_length, head_a, head_b = fast_forward_larger_list(list_a, list_b)

    if head_a == head_b:
        return head_a

    for _ in xrange(0, min_length):
        if head_a.next == head_b.next:
            return head_a.next
        else:
            head_a = head_a.next
            head_b = head_b.next

    return None


def test_normal_intersection():
    c1 = ListNode(5)
    c2 = ListNode(6)
    c3 = ListNode(7)

    c1.next = c2
    c2.next = c3

    a1 = ListNode(0)
    a2 = ListNode(1)

    a1.next = a2
    a2.next = c1

    b1 = ListNode(2)
    b2 = ListNode(3)
    b3 = ListNode(4)

    b1.next = b2
    b2.next = b3
    b3.next = c1

    assert fast_forward_linked_list(b1, 1) == b2
    assert linked_list_len(c1) == 3
    assert linked_list_len(a1) == 5
    assert linked_list_len(b1) == 6
    assert find_intersection_node(a1, b1) == c1


def test_one_way_intersection():
    c1 = ListNode(5)
    c2 = ListNode(6)
    c3 = ListNode(7)

    a1 = ListNode(0)

    a1.next = c1
    b1 = c1

    assert find_intersection_node(a1, b1) == c1
