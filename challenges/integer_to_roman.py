
def int_to_roman(num):
    symbols = []
    roman_literals = [
        (1000, 'M'),
        (500, 'D'),
        (100, 'C'),
        (50, 'L'),
        (10, 'X'),
        (5, 'V'),
        (1, 'I')
    ]

    for i in range(0, len(roman_literals)):
        value, symbol = roman_literals[i]

        count = num / value
        symbols += count * [symbol]
        num = num % value

    numeral = ''.join(symbols)
    print(numeral)
    numeral = numeral.replace('DCCCC', 'CM')  # 900
    numeral = numeral.replace('CCCC', 'CD')  # 400

    numeral = numeral.replace('LXXXX', 'XC')  # 90
    numeral = numeral.replace('XXXX', 'XL')  # 40

    numeral = numeral.replace('VIIII', 'IX')  # 9
    numeral = numeral.replace('IIII', 'IV')  # 4

    return numeral


def test_int_to_roman():
    assert int_to_roman(1990) == 'MCMXC'
    assert int_to_roman(4) == 'IV'
    assert int_to_roman(6) == 'VI'
    assert int_to_roman(10) == 'X'
    assert int_to_roman(9) == 'IX'
    assert int_to_roman(1) == 'I'
    assert int_to_roman(5) == 'V'
    assert int_to_roman(14) == 'XIV'
    assert int_to_roman(20) == 'XX'
    assert int_to_roman(2014) == 'MMXIV'
    assert int_to_roman(1490) == 'MCDXC'


if __name__ == '__main__':
    test_int_to_roman()
