class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return 'Node<{},{}>'.format(self.val, self.next)


class ListNodePartition:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def append(self, node):
        node.next = None
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = self.head

    def join(self, other_partition):
        if self.tail:
            self.tail.next = other_partition.head
            return self.head
        else:
            return other_partition.head


def partition_list(head, pivot):
    part_right = ListNodePartition()
    part_left = ListNodePartition()

    while head:
        node = head
        head = head.next

        if node.val >= pivot:
            part_right.append(node)
        else:
            part_left.append(node)

    return part_left.join(part_right)


def test_unequal_partitions():
    n1 = ListNode(4)
    n2 = ListNode(5)
    n3 = ListNode(6)

    n1.next = n2
    n2.next = n3

    head = partition_list(n1, 3)

    assert head == n1
    head = head.next
    assert head == n2
    head = head.next
    assert head == n3


def test_no_elem_list():
    assert partition_list(None, 1) is None


def test_one_elem_list():
    n1 = ListNode(1)
    head = partition_list(n1, 1)
    assert head == n1
    assert head.next is None


def test_normal_partition():
    n1 = ListNode(1)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n4 = ListNode(2)
    n5 = ListNode(5)
    n6 = ListNode(2)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6

    head = partition_list(n1, 3)
    print(head)
    assert head == n1
    head = head.next
    assert head == n4
    head = head.next
    assert head == n6
    head = head.next
    assert head == n2
    head = head.next
    assert head == n3
    head = head.next
    assert head == n5
