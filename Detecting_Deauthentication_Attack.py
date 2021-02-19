from scapy.config import conf
conf.ipv6_enabled = False
from scapy.all import *
# importing scapy for packet analyzing
import time,datetime

print("Waiting for trigger...")
# importing datetime for timestamp
def detect_deauth_attack(pkt):
	# Deauth attack detecting function
	if pkt.haslayer(Dot11Deauth):
		# Analyzing if packet contain Deauth layer
		time=datetime.datetime.today()
		# Generating timestamp
		a= ' [ ' +  str(time)+ ' ] '+  ' Deauthentication Attack Detected Against Mac Address: ' +   str(pkt.addr2).swapcase()    
		print(a)
		file1 = open(r"/home/pi/Desktop/python2txtTEST.txt","w+") 
		file1.write(a)
		file1.close()
sniff(prn=detect_deauth_attack,count=0)
# Sniffing packet and sending them to deauth detect function
