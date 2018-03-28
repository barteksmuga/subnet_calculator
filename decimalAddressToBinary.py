def decimal_to_binary(number):
    return int(bin(int(number))[2:])


def convert_dec_address_to_bin(address):
    dec_address = address.split(".")
    bin_addr = ''
    for address in dec_address:
        bin_addr += str(decimal_to_binary(address)) + ' '
    return bin_addr[:-1]
