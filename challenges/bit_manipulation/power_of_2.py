def count_one_bits(num):
    one_bits = 0

    while num > 0:
        if num & 1:
            one_bits += 1
        num = num >> 1

    return one_bits


def power_of_two(num):
    return count_one_bits(num) == 1


def test_one_bits():
    assert count_one_bits(1) == 1
    assert count_one_bits(2) == 1
    assert count_one_bits(3) == 2
    assert count_one_bits(4) == 1
    assert count_one_bits(5) == 2


def test_power_of_two():
    assert power_of_two(1)
    assert power_of_two(2)
    assert not power_of_two(3)
    assert power_of_two(4)
    assert not power_of_two(5)
    assert not power_of_two(6)
    assert power_of_two(8)
    assert power_of_two(16)
    assert power_of_two(32)
