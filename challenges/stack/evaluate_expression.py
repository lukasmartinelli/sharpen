"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or
another expression.

    ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
    ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""


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
    numbers = []
    for expr in notation:
        if is_operand(expr):
            right = numbers.pop()
            left = numbers.pop()
            result = eval(left, right, expr)
            numbers.append(result)
        else:
            numbers.append(int(expr))

    return numbers.pop()


eval_rpn = eval_reverse_polish_notation


def test_simple_expression():
    assert eval_rpn(["2", "1", "+"]) == 3


def test_reducable_expression():
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9


def test_complex_reducable_expression():
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6
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
