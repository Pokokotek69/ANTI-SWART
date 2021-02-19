import time
import sys
a = 1
#b = i
print("STARTING CLEAR")
while a == 1:
        file1 = open(r"/home/pi/Desktop/python2txtTEST.txt","w+")
        file1.write("No suspicious activity")
        for remaining in range(10, 0, -1):
    		sys.stdout.write("\r")
    		sys.stdout.write("{:2d} seconds remaining.".format(remaining))
    		sys.stdout.flush()
    		time.sleep(1)
	sys.stdout.write("\rCLEARED!            \n")
