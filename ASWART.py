import time
import os
import subprocess 
from progress.bar import ShadyBar


print("\n")

print("STARTING...")
print("\n")
time.sleep(1)

with ShadyBar('STARTING ANTI-SWART', max=10) as bar:
    for i in range(10):
        time.sleep(0.1)
        bar.next()


os.system("cat SWART.txt")
time.sleep(1)
os.system("cat BSWART.txt")
print("\n")
print("\n")
time.sleep(1)
os.system("cat ASWART.txt")
print("\n")
time.sleep(2)


print("Starting CLEAR")
time.sleep(1)
subprocess.call('lxterminal -e python clear.py &', cwd='/home/pi/Desktop/AWS_IOT', shell =True)
time.sleep(2)
#os.system(a)
print("Starting DETECT")
subprocess.call('lxterminal -e python Detecting_Deauthentication_Attack.py &', cwd='/home/pi/Desktop/AWS_IOT', shell =True)

time.sleep(2)

print("Starting Send_Only")
time.sleep(4)
print("\n")
print("No suspicious activity... Waiting for detection...")
os.system("sudo python send_only.py")





