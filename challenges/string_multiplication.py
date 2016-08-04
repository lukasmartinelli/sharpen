def multiply(left, right):
    if len(left) > 1:
        raise ValueError("The left operand must be smaller than < 10")

    left_operand = int(left)
    take_over = 0
    # we can use dequeue later for inserting at start fast
    total = ""

    for c in right:
        right_operand = int(c)
        result = left_operand * right_operand

        keep = (result + take_over) % 10
        total = str(keep) + total
        take_over = result / 10

    if take_over > 0:
        total = str(take_over + int(total))

    return total


def test_multiply():
    assert multiply("7", "73") == "511"
