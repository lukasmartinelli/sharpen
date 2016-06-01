def count_set_bits(num):
    set_bits = 0

    while num != 0:
        if num & 0b1 == 0b1:
            set_bits += 1
        num = num >> 1

    return set_bits

assert count_set_bits(0b1) == 1
assert count_set_bits(0b101) == 2
assert count_set_bits(0b10110101) == 5
assert count_set_bits(0b00000000000000000000000000001011) == 3



def reverse_bits(num, i, j):
    # Are the first and last bit different?
    test = num ^ 0b10000000000000000000000000000001

    if test == 0b00000000000000000000000000000001:
        num = num | (1num << i)

        num = num ^ 0b10000000000000000000000000000001

    if test == 0b10000000000000000000000000000000:
        num = num ^ 0b10000000000000000000000000000000

    return num

print(bin(reverse_bits(0b00000000000000000000000000000110)))
