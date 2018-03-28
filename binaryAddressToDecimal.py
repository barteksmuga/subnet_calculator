def binary_to_decimal(x):
    return int(str(x), 2)


def convert_bin_address_to_dec(bin_address):
    bin_address = bin_address.split(' ')
    dec_addr = ''
    for i in bin_address:
        dec_addr += str(binary_to_decimal(i)) + "."

    return dec_addr[:-1]