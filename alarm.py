#!/usr/bin/python
#A simple alarm/timer program implemented in python.
#Created on Sunday, January 20, 2013
 
import time
import sys
 
time.sleep(int(sys.argv[1]))
 
print('\a')
print(sys.argv[1] + ' seconds have passed.')
