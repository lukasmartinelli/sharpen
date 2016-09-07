def generate_parenthesis(n):
    """
    Given n pairs of parentheses, write a function to generate all
    combinations of well-formed parentheses.

    For n=3 the solution is:

        "((()))", "(()())", "(())()", "()(())", "()()()"

    For each opening bracket we can either start a new opening
    bracket or close it and track back.
    """
    if n == 0:
        return []

    def all_combinations(braces, opening=0, closing=0):
        if len(braces) >= 2*n:
            yield braces
            return

        if opening < n:
            for c in all_combinations(braces + ["("], opening+1, closing):
                yield c

        if closing < opening:
            for c in all_combinations(braces + [")"], opening, closing+1):
                yield c

    return ["".join(p) for p in all_combinations([])]


def test_generate_parenthesis():
    assert generate_parenthesis(0) == []
    assert generate_parenthesis(1) == ["()"]
    assert generate_parenthesis(2) == ["(())", "()()"]
    assert generate_parenthesis(3) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ]

    assert len(generate_parenthesis(4)) == 14
    assert generate_parenthesis(4) == [
        "(((())))",
        "((()()))",
        "((())())",
        "((()))()",
        "(()(()))",
        "(()()())",
        "(()())()",
        "(())(())",
        "(())()()",
        "()((()))",
        "()(()())",
        "()(())()",
        "()()(())",
        "()()()()"
    ]
