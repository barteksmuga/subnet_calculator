def broadcast_address(ip, mask):
    ip = ip.split('.')
    mask = mask.split('.')
    broad_addr = ''
    for i in range(len(ip)):
        broad_addr += str(255 - int(mask[i]) + int(ip[i])) + '.'
    broad_addr = broad_addr.split('.')
    for i in range(len(broad_addr)):
        if broad_addr[i] > str(255):
            broad_addr[i] = str(255)
    return '.'.join(broad_addr[:-1])
