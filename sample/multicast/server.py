#!/usr/bin/env python

import socket
import struct
import time
#224.0.0.0-239.255.255.255
MULTICAST_GRP = "235.192.168.99"
MULTICAST_PORT = 9999
def main():
	sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	sock.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL,32)
	while 1:
		data = time.strftime('(%Y-%m-%d %H:%M:%S)')
		sock.sendto(data,(MULTICAST_GRP,MULTICAST_PORT))
		print data
		time.sleep(5)


if __name__ == '__main__':
	main()
