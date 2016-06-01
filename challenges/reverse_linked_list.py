class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return 'Node<{},{}>'.format(self.value, self.next)


def reverse_in_place(head):
    if head is None:
        raise ValueError('Linked list needs at least one node')

    if head.next is None:
        return head

    previous_node = head
    current_node = head.next
    head.next = None

    while True:
        next_node = current_node.next
        current_node.next = previous_node

        if next_node is None:
            break

        previous_node = current_node
        current_node = next_node

    return current_node


def create_list():
    nodes = [Node(i) for i in range(0, 10)]
    for i in range(1, len(nodes)):
        nodes[i-1].next = nodes[i]

    return nodes[0]

head = create_list()
print(head)
head = reverse_in_place(head)
print(head)
