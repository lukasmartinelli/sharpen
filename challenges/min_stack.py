class MinStack:
    "2 * O(n) space"
    def __init__(self):
        self.min_elements = []
        self.ordered_elements = []

    def push(self, x):
        "O(1)"
        if len(self.min_elements) == 0 or x < self.min_elements[-1]:
            self.min_elements.append(x)
        else:
            self.min_elements.append(self.min_elements[-1])

        self.ordered_elements.append(x)

    def pop(self):
        "O(1)"
        if len(self.ordered_elements) > 0:
            self.min_elements.pop()
            self.ordered_elements.pop()

    def top(self):
        "O(1)"
        if len(self.ordered_elements) > 0:
            return self.ordered_elements[-1]
        else:
            return -1

    def getMin(self):
        "O(1)"
        if len(self.min_elements) > 0:
            return self.min_elements[-1]
        else:
            return -1


def test_min_stack():
    stack = MinStack()

    stack.pop()
    assert stack.top() == -1
    assert stack.getMin() == -1

    stack.push(10)
    stack.push(3)
    assert stack.getMin() == 3
    stack.pop()
    assert stack.getMin() == 10

    stack.push(5)
    assert stack.getMin() == 5

    stack.push(6)
    assert stack.getMin() == 5

    stack.push(3)
    assert stack.getMin() == 3
    stack.pop()
    assert stack.getMin() == 5
