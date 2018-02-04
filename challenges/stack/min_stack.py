class MinStack:
    """
    Implement a stack that supports push, pop, top and getMin in O(1) time.
    """
    def __init__(self):
        self.elements = []

    def push(self, x):
        "O(1)"
        if len(self.elements) == 0:
            self.elements.append((x, x))
        else:
            self.elements.append((x, min(x, self.getMin())))

    def pop(self):
        "O(1)"
        if len(self.elements) > 0:
            return self.elements.pop()[0]

    def top(self):
        "O(1)"
        if len(self.elements) > 0:
            return self.elements[-1][0]
        else:
            return -1

    def getMin(self):
        "O(1)"
        if len(self.elements) > 0:
            return self.elements[-1][1]
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
