def network_class(ip_address):
    ip = ip_address.split(".")
    if int(ip[0]) < 127:
        return "A"
    elif 128 <= int(ip[0]) < 192:
        return "B"
    elif 192 <= int(ip[0]) < 224:
        return "C"
    elif 224 <= int(ip[0]) < 240:
        return "D"
    elif 240 <= int(ip[0]) <= 255:
        return "E"


def get_network_addres(ip, mask):
    ip_parts = ip.split('.')
    mask_parts = mask.split('.')
    network_addr = ''
    for i in range(len(mask_parts)):
        network_addr += str(int(ip_parts[i]) & int(mask_parts[i])) + '.'
    return network_addr[:-1]
