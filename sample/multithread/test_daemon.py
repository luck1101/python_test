#/usr/bin/env python

import threading
import time
class Mythread(threading.Thread):
	def __init__(self,name):
		threading.Thread.__init__(self)
		self.name = name
		print "thread %s init......"%name

	def run(self):
		print "thread %s start......."%self.name
		i = 10
		while i:
			print "thread %s sleep........"%self.name
			time.sleep(1)
			i -= 1
		print "thread %s terminates........"%self.name


def main():
	print "%s create 2 thread"%threading.currentThread().getName()
	#thread1 = Mythread("No1")
	thread2 = Mythread("No2")
	thread2.setDaemon(True)
	#thread1.start()
	thread2.start()
	print "main thread sleep 3 second exit"
	time.sleep(3)
	print "main thread exit\n"

if __name__ == "__main__":
	main()




