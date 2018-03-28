from binaryAddressToDecimal import convert_bin_address_to_dec
from hosts import is_ip_valid, get_ip_with_cidr, min_host_address, max_host_address, hosts_number, get_cidr_from_ip_with_cidr,\
    get_ip_from_ip_with_cidr

import networkInfo
import broadcastAddress
import writeToJson
import cidrToBinary
import decimalAddressToBinary

import sys


if len(sys.argv) > 1:
    # 198.167.0.12/24
    # 148.27.232.140/18
    ip = sys.argv[1]
else:
    ip = get_ip_with_cidr()

if is_ip_valid(ip):

    mask_bin = cidrToBinary.cidr_to_binary(get_cidr_from_ip_with_cidr(ip))
    mask = convert_bin_address_to_dec(mask_bin)

    ip = get_ip_from_ip_with_cidr(ip)

    network_dec = networkInfo.get_network_addres(ip,mask)
    network_class = networkInfo.network_class(ip)

    broadcast_addr = broadcastAddress.broadcast_address(ip,mask)
    broadcast_addr_bin = decimalAddressToBinary.convert_dec_address_to_bin(broadcast_addr)

    min_host = min_host_address(network_dec)
    min_host_bin = decimalAddressToBinary.convert_dec_address_to_bin(min_host)

    max_host = max_host_address(broadcast_addr)
    max_host_bin = decimalAddressToBinary.convert_dec_address_to_bin(max_host)

    hosts_num = hosts_number(min_host,max_host)
    hosts_num_bin = decimalAddressToBinary.decimal_to_binary(hosts_num)

    data = {
        'ip': ip,
        'adres_sieci': network_dec,
        'klasa_sieci': network_class,
        'maska_sieci': [mask,mask_bin],
        'adres_broadcast':[broadcast_addr,broadcast_addr_bin],
        'pierwszy_host':[min_host,min_host_bin],
        'ostatni_host':[max_host,max_host_bin],\
        'ilosc_hostow':[hosts_num, hosts_num_bin]}

    writeToJson.write_to_json("data.json",data)

    print "ip:\t\t\t\t {0}\n" \
          "adres_sieci:\t {1}\n" \
          "klasa_sieci:\t {2}\n" \
          "maska_sieci:\t {3}\n\t\t\t\t {4}\n" \
          "adres_broadcast: {5}\n\t\t\t\t {6}\n" \
          "pierwszy_host:\t {7}\n\t\t\t\t {8}\n" \
          "ostatni_host:\t {9}\n\t\t\t\t {10}\n" \
          "ilosc_hostow:\t {11}\n\t\t\t\t {12}"\
        .format(ip, network_dec, network_class, mask, mask_bin, broadcast_addr, broadcast_addr_bin,
        min_host, min_host_bin, max_host, max_host_bin, hosts_num, hosts_num_bin)
else:
    print "Invalid IP address!"