from getmac import get_mac_address as gma
import os
import sys
import socket
import struct
import fcntl

index = []
mac_addr = ""
net_interface = ""

def args_func():
	global mac_addr, net_interface
	if len(sys.argv) > 2:
		mac_addr = sys.argv[1]
		net_interface = sys.argv[2]
	else:
		print("[-] Invalid Format! Example: sudo python3 mac_changer.py <mac> <interface>")
		
def convert_to_hex_func():
	global mac_addr

	args_func()
	print("Current MAC: ", gma())

	mac_addr = mac_addr.split(":")
	mac_addr = "".join(mac_addr)
	byte_mac = bytes.fromhex(mac_addr)
	print("Hex Format MAC: ", byte_mac)

	return byte_mac

def socket_func():
	global net_interface
	
	byte_mac = convert_to_hex_func()

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	#kernel "change mac address" command
	SIOCSIFHWADDR = 0x8924


	##c-struct packaging for OS
	ifr = struct.pack('16sH6s8s', net_interface.encode('utf-8'), 1, byte_mac, b'\x00'*8)

	try:
		# Send packet
		fcntl.ioctl(s.fileno(), SIOCSIFHWADDR, ifr)
		print("[+] MAC Address Changed Successfully!")
	except Exception as e:
		print(f"[+] An Error Occured: {e}")  

if __name__ == '__main__':
	if os.geteuid() != 0:
		print("[-] The script must be run as root priveleges! Please run: 'sudo python3 mac_changer.py'")
		sys.exit(1)
		
	socket_func()
