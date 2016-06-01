def is_palindrome(sentence):
    def normalize():
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                    'w', 'x', 'y', 'z']
        digits = [str(digit) for digit in range(0, 10)]
        alphanum = set(alphabet + digits)

        for c in sentence:
            c = c.lower()
            if c in alphanum:
                yield c

    normalized_sentence = list(normalize())
    return normalized_sentence == list(reversed(normalized_sentence))

assert is_palindrome("A man, a plan, a canal: Panama")
