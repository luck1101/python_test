#!/usr/bin/env python

import socket
import struct

MULTICAST_GRP = "235.192.168.99"
MULTICAST_PORT = 9999


def main():
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.bind(('',MULTICAST_PORT))
	mreq = struct.pack("=4sl",socket.inet_aton(MULTICAST_GRP),socket.INADDR_ANY)
	s.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)
	while 1:
		print "recvied from server" + s.recv(1024)
if __name__ == "__main__":
	main()