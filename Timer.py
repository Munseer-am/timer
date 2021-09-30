#! bin/env python3

"""This timer is limited to 60mins.You can extend time if want by changing the 25th line of code."""
"""This timer only supports seconds format."""

import time
import sys

print("""  __  __
 |  \/  |_   _ _ __  ___  ___  ___ _ __
 | |\/| | | | | '_ \/ __|/ _ \/ _ \ '__|
 | |  | | |_| | | | \__ \  __/  __/ |
 |_|  |_|\__,_|_| |_|___/\___|\___|_|""")

def countdown(t):
	while t:
		mins,secs = divmod(t,60)
		
		timer = '{:02d}:{:02d}'.format(mins,secs)
		print(timer,end='\r')
		time.sleep(1)
		t -= 1
	print(' time up')
	
t = int(input(' Enter time in seconds: '))
if t > 3600:
	sys.exit()
else:
	countdown(int(t)
	
