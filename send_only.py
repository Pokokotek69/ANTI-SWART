import time
import subprocess
i = 1

while i == 1:
	f = open("/home/pi/Desktop/python2txtTEST.txt", "r")
	a = f.read()
	if 'Deauthentication' in a:
		print(a)
		subprocess.call("/home/pi/Desktop/AWS_IOT/start.sh", shell=True)
		time.sleep(1) 
		print("Exiting...")
		
