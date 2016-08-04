import heapq


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


class LinkedListHeap():
    def __init__(self, lists):
        self.heap = []

        for list_head in lists:
            heapq.heappush(self.heap, (list_head.val, list_head))

    def pop_min(self):
        """Get and remove node with min value"""
        try:
            _, min_node = heapq.heappop(self.heap)
        except IndexError:
            return None

        next_node = min_node.next
        if next_node:
            heapq.heappush(self.heap, (next_node.val, next_node))

        return min_node


def merge_k_lists(lists):
    heap = LinkedListHeap(lists)
    head = ListNode('dummy')
    tail = head

    min_node = heap.pop_min()
    while min_node:
        min_node.next = None
        tail.next = min_node
        tail = tail.next
        min_node = heap.pop_min()

    return head.next


def test_merge_k_sorted_lists():
    a = LinkedList([1, 10, 20])
    b = LinkedList([4, 11, 13])
    c = LinkedList([3, 8, 9])

    lists = [a, b, c]

    merged_list = merge_k_lists(lists)
    assert merged_list == LinkedList([1, 3, 4, 8, 9, 10, 11, 13, 20])
