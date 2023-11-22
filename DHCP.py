#!/usr/bin/python3

# Import modules
from scapy.all import Ether, IP, UDP, BOOTP, DHCP, sendp

# Set color variables
Green = "\033[1;32m"
Blue = "\033[1;34m"
White = "\033[0m"

def discover(src_mac,dst_mac,interface):
    # Forge packet
    dst_mac_bytes = (int(dst_mac.replace(":", ""), 16).to_bytes(6, "big"))
    dhcp_discover = Ether(src=src_mac) / IP(src="0.0.0.0", dst="255.255.255.255") / UDP(sport=68, dport=67) / BOOTP(chaddr=dst_mac_bytes, xid=0x01020304, flags=0x8000) / DHCP(options=[("message-type", "discover"), "end"])
    # Send
    sendp(dhcp_discover, iface=interface, verbose=0)
    # Output
    print(f"{Green}[+]{White} Send - DHCP Discover")
    
def offer():
    print('pass')

def request():
    print('pass')

def ack():
    print('pass')