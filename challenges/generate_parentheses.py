def matching_parens(a, b):
    return (
        (a == '(' and b == ')') or
        (a == '{' and b == '}') or
        (a == '[' and b == ']')
    )


def has_valid_parens(text):
    stack = []

    for c in text:
        if c in ['(', '[', '{']:
            stack.append(c)
        elif c in [')', ']', '}']:
            closing_parens = c

            try:
                opening_parens = stack.pop()
            except IndexError:
                return False

            if not matching_parens(opening_parens, closing_parens):
                return False

    return len(stack) == 0


def test_paren():
    assert not has_valid_parens('([')
    assert has_valid_parens('([{}])')
    assert has_valid_parens('(([]){})')
    assert not has_valid_parens('([)')
    assert not has_valid_parens('((((([{()}[]]]{{{[]}}})))))')
