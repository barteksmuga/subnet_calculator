import socket
import re


def get_ip_address():
    return socket.gethostbyname(socket.gethostname())


def is_ip_valid(ip_addr):
    ip_parts = ip_addr.split("/")
    regex = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    parts = ip_parts[0].split('.')
    return is_cidr_valid(ip_parts[1]) and re.match(regex,ip_parts[0]) and len(parts) == 4 and all(0 <= int(part) < 256 for part in parts)


def is_cidr_valid(cidr):
    return 0 <= int(cidr) < 33


def get_ip_with_cidr():
    return socket.gethostbyname(socket.gethostname()) + "/24"


def get_ip_from_ip_with_cidr(ip):
    return (ip.split('/'))[0]


def get_cidr_from_ip_with_cidr(ip):
    return (ip.split('/'))[1]


def min_host_address(network_address):
    network_address = network_address.split('.')
    network_address[3] = str(int(network_address[3]) + 1)
    return '.'.join(network_address)


def max_host_address(broadcast_address):
    broadcast_address = broadcast_address.split(".")
    broadcast_address[3] = str(int(broadcast_address[3]) - 1)
    return '.'.join(broadcast_address)


def hosts_number(min_host_address, max_host_address):
    min_host_parts = min_host_address.split(".")
    max_host_parts = max_host_address.split(".")
    nets_number = 1 + (int(max_host_parts[2])-int(min_host_parts[2]))
    if nets_number != 1:
        nets_number = nets_number - 2
        host_number = (256 - int(min_host_parts[3])) + (nets_number * 256) + (int(max_host_parts[3])+1)
    else:
        host_number = (int(max_host_parts[3]) - int(min_host_parts[3])) + 1
    return host_number
