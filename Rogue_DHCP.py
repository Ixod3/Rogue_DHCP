#!/usr/bin/python3

# Import modules
import fct_dhcp
import fct_random
import fct_scapy
import fct_os
import argparse
import time
import os

# Set color variables
Green = "\033[1;32m"
Blue = "\033[1;34m"
White = "\033[0m"

# Parse command
parser = argparse.ArgumentParser()
parser.add_argument("-i","--interface", required=True, help="Interface network")
args = parser.parse_args()

# Detect interface wire/wireless
if args.interface.startswith('w'):
    # For wireless connexion
    print(f"{Blue}[~]{White} Detect Wireless interface")
    fct_os.change_mac(args.interface)
    actual_mac = fct_os.get_mac(args.interface)
else:
    # For wire connexion
    print(f"{Blue}[~]{White} Detect Wire interface")
    fct_os.set_promiscuous(args.interface)
    actual_mac = fct_os.get_mac(args.interface)

# Listener discover start
sniff_packet = fct_scapy.listener_start(actual_mac)

# DHCP Discover
xid = fct_random.transaction_id()
fct_dhcp.discover(actual_mac, xid, args.interface)

# Listener discover join
legit_dhcp_ip = fct_scapy.listener_join(sniff_packet)
print (f"{Green}[+]{White} DHCP Server IP address is {legit_dhcp_ip}")
