from scapy.all import *
import sys
import socket
import struct

ip_layer = IP(src = "192.168.222.1", dst="192.168.222.2", chksum = 0xbfab)
icmp_layer = ICMP(type = 8, code = 0)
payload = Raw("Hi from ICMP")

ip_layer.show()
icmp_layer.show()

pkt = ip_layer / icmp_layer / payload
pkt.show()

response = sr1(pkt)
response.show()
