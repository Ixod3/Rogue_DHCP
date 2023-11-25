#!/usr/bin/python3

# Import modules
import scapy.all as scapy

# Set color variables
Green = "\033[1;32m"
Blue = "\033[1;34m"
White = "\033[0m"

def discover(src_mac, xid, interface):
    # Forge packet
    src_mac_bytes = (int(src_mac.replace(":", ""), 16).to_bytes(6, "big"))
    dhcp_discover = scapy.Ether(src=src_mac,dst="ff:ff:ff:ff:ff:ff") / scapy.IP(src="0.0.0.0", dst="255.255.255.255") / scapy.UDP(sport=68, dport=67) / scapy.BOOTP(chaddr=src_mac_bytes, xid=xid, flags=0x0000) / scapy.DHCP(options=[("message-type", "discover"), ('client_id', src_mac), ('param_req_list',[1,2,3,6,12,15,26,28,33,40,41,42,119,121]),('hostname',f"user_X"), "end"])
    # Send
    scapy.sendp(dhcp_discover, iface=interface, verbose=0)
    # Output
    print(f"{Green}[+]{White} Send - DHCP Discover")
    
def offer():
    print('pass')

def request():
    print('pass')

def ack():
    print('pass')