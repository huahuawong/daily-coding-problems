n = int('4294967292')


def reversebit(n):
    # Convert the given integer to an 32-bit binary string;
    bit_str = '{0:032b}'.format(n)
    # now we reserve the string
    reverse_str = bit_str[::-1]
    # convert it back to integer from base 2 to base 10
    return int(reverse_str, 2)

print(reversebit(n))




