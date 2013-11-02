#!/usr/bin/env python

import threading
count = 0
def test_lock():
	for i in range(5):
		count += 1


def test_event():
	event = threading.Event()
	print "event initially value",event.isSet()
	print event.wait(5)
	print "wait pass...."
	print "event wait after value",event.isSet()


def main():
	print "count = %d"%threading.active_count()
	current = threading.currentThread()
	print "current thread name =%s"%current.getName()
	print "thread is_alive %s"%current.is_alive()
	
if __name__ == "__main__":
	main()
	test_event()