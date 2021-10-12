#! usr/bin/env python3

"""This timer only supports seconds format."""
__author__ = "Munseer"

# importing required modules
import time
import sys

# printing name of author
print("""  __  __
 |  \/  |_   _ _ __  ___  ___  ___ _ __
 | |\/| | | | | '_ \/ __|/ _ \/ _ \ '__|
 | |  | | |_| | | | \__ \  __/  __/ |
 |_|  |_|\__,_|_| |_|___/\___|\___|_|""")
print("\n This script is created by Munseer")

# codes for timer 
def countdown(t):
	while t:
		mins,secs = divmod(t,60)
		
		timer = '{:02d}:{:02d}'.format(mins,secs)
		print(timer,end='\r')
		time.sleep(1)
		t -= 1
	print(' time up')

# user input	
t = int(input(' Enter time in seconds: '))

# time limit
if t > 3600:
        print(" Limit Exceeded")
	sys.exit()
else:
	countdown(int(t)
	
