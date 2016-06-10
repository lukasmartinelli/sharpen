import collections


def reduce_notation(notation):
    reduced_notation = collections.deque()

    if len(notation) == 1:
        return notation

    while len(notation) > 2:
        op = notation.pop()
        right = notation.pop()
        left = notation.pop()

        if not is_operand(op):
            reduced_notation.appendleft(op)
            reduced_notation.appendleft(right)
            reduced_notation.appendleft(left)
        elif is_operand(left):
            notation.append(left)
            reduced_notation.appendleft(op)
            reduced_notation.appendleft(right)
        elif is_operand(right):
            notation.append(left)
            notation.append(right)
            reduced_notation.appendleft(op)
        else:
            result = eval(int(left), int(right), op)
            reduced_notation.appendleft(result)

    reduced_notation.extendleft(notation)
    return reduced_notation


def is_operand(expr):
    return expr in ['+', '-', '/', '*']


def eval(left, right, op):
    if op == '+':
        return left + right
    elif op == "-":
        return left - right
    elif op == "/":
        return left / right
    elif op == "*":
        return left * right
    else:
        raise ValueError('Operand {} not supported'.format(op))


def eval_reverse_polish_notation(notation):
    while len(notation) > 2:
        notation = reduce_notation(notation)
        print(notation)

    if len(notation) > 1:
        raise ValueError('Notation not reducable')

    return notation[0]


eval_rpn = eval_reverse_polish_notation


def test_simple_expression():
    assert eval_rpn(["2", "1", "+"]) == 3


def test_reducable_expression():
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9


def test_complex_reducable_expression():
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6


def test_complex_reducable_expression():
    assert eval_rpn(["4", "13", "3", "+", "5", "/", "+"]) == 7


def test_long_expression():
    assert eval_rpn([
        "-2", "-1", "2", "+", "-1", "-", "-", "2", "-2", "1",
        "-", "+", "-", "-2", "-2", "-", "-1", "2", "-2", "-", "-2", "-1", "+",
        "1", "1", "-", "-1", "+", "1", "*", "*", "2", "+", "*", "-", "-2", "1",
        "-2", "*", "+", "-2", "*", "1", "*", "-", "*", "*"]) == 0


def test_minus_expression():
    assert eval_rpn([
        "1", "-1", "2", "+", "2", "-", "-1", "1", "*", "-", "-2", "*", "*",
        "2", "-2", "-2", "*", "-", "+", "-2", "1", "-", "1", "-", "*", "2",
        "-", "-1", "2", "1", "*", "*", "-"]) == 8
