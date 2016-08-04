symbol_lookup = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def roman_to_int(numeral):
    if len(numeral) == 0:
        return 0

    current_value = symbol_lookup.get(numeral[0], 0)

    if len(numeral) > 1:
        lookahead = symbol_lookup.get(numeral[1], 0)
        if lookahead > current_value:
            return roman_to_int(numeral[1:]) - current_value

    return current_value + roman_to_int(numeral[1:])


def test_roman_to_int():
    assert roman_to_int('XIV') == 14
    assert roman_to_int('XX') == 20
    assert roman_to_int('MMXIV') == 2014
    assert roman_to_int('MCMXC') == 1990
