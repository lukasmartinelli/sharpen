def zip_longest_linked_lists(a, b):
    default = ListNode(0)
    while a or b:
        if a and b:
            yield a, b
            a = a.next
            b = b.next
        elif a:
            yield a, default
            a = a.next
        elif b:
            yield default, b
            b = b.next


def add_numbers(term_a, term_b):
    results = AdditionLinkedList()

    for node_a, node_b in zip_longest_linked_lists(term_a, term_b):
        results.add(node_a, node_b)

    results.add_carryover()

    return results.head


class AdditionLinkedList():

    def __init__(self):
        self.head = None
        self.tail = self.head
        self.carryover = 0

    def add(self, term_a, term_b):
        result = term_a.val + term_b.val + self.carryover
        self.carryover = result / 10
        digit = result % 10

        new_node = ListNode(digit)
        self.append(new_node)

    def add_carryover(self):
        if self.carryover > 0:
            self.append(ListNode(self.carryover))
            self.carryover = 0

    def append(self, new_node):
        if self.tail:
            self.tail.next = new_node
            self.tail = self.tail.next
        else:
            self.head = new_node
            self.tail = self.head


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


def test_simple_addition():
    a = LinkedList([2, 4, 3])
    b = LinkedList([3, 5, 2])
    assert add_numbers(a, b) == LinkedList([5, 9, 5])


def test_addition_carryover():
    a = LinkedList([2, 4, 3])
    b = LinkedList([5, 6, 4])
    assert add_numbers(a, b) == LinkedList([7, 0, 8])


def test_addition_multi_carryover():
    a = LinkedList([9, 3, 5])
    b = LinkedList([2, 8, 9])
    assert add_numbers(a, b) == LinkedList([1, 2, 5, 1])


def test_add_unequal_numbers():
    a = LinkedList([9, 9, 1])
    b = LinkedList([1])
    assert add_numbers(a, b) == LinkedList([0, 0, 2])

    c = LinkedList([1, 5])
    d = LinkedList([5, 5, 9, 9])
    assert add_numbers(c, d) == LinkedList([6, 0, 0, 0, 1])
