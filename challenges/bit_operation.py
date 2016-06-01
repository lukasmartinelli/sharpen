

def is_even(num):
    return (num & 0b1) == 0b0


def is_bit_set(num, n):
    return (num << n) == 0b0

print('Is even', is_even(0b1111))
print('Is odd', is_even(0b1110))

print('Had 4th bit set', is_bit_set(0b100, 4))
print('Has 3rd bit set', is_bit_set(0b110, 3))
print('Has 1st bit set', is_bit_set(0b10, 1))
