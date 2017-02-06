from socket import *

s = socket(AF_INET, SOCK_RAW, IPPROTO_TCP)
s.bind(('127.0.0.1',8000))

while True:

    data = s.recv(2048)

    print(data)

    ihl = ord(data[0]) & 15
    ip_payload = data[ihl * 4:]


    if (ord(ip_payload[13]) & 18) == 2:
        src_addr = inet_ntoa(data[12:16])
        dst_addr = inet_ntoa(data[16:20])

        # Could use struct.unpack, might be clearer
        src_port = (ord(ip_payload[0]) << 8) + ord(ip_payload[1])
        dst_port = (ord(ip_payload[2]) << 8) + ord(ip_payload[3])

        src_str = (src_addr + ':' + str(src_port)).ljust(22)
        dst_str = (dst_addr + ':' + str(dst_port))

        print('{} => {}'.format (src_str, dst_str))