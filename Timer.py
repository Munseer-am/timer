#! bin/env python3
import time
import sys

def countdown(t):
	while t:
		mins,secs = divmod(t,60)
		
		timer = '{:02d}:{:02d}'.format(mins,secs)
		print(timer,end='\r')
		time.sleep(1)
		t -= 1
	print(' time up')
	
t = int(input(' Enter time in seconds: '))
if t > 1000:
	sys.exit()
else:
	countdown(int(t))
	
