#!/usr/bin/python
# thread module is not supported in pyton 3
import threading
import time

def print_time(threadName,delay):
	count = 0
	while count<5:
		time.sleep(delay)
		count+=1
		print("%s: %s",threadName,time.ctime(time.time()))

# creating thread
try:
	threading.start_new_thread(print_time,("thread -1",2,))
	threading.start_new_thread(print_time,("thread -2",3,))
except:
	print("error unable to start thread")

while 1:
	pass
