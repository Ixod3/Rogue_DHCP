#!/usr/bin/python3

# Import modules
import fct_dhcp
import fct_random
import fct_scapy
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

# Set promiscuitous interface
os.system(f"sudo ifconfig {args.interface} promisc")

# Listener discover start
sniff_packet = fct_scapy.listener_start("44:af:28:d9:46:a3")

# DHCP Discover
xid = fct_random.rand_transaction_id()
fct_dhcp.discover("44:af:28:d9:46:a3", xid, args.interface)

# Listener discover join
legit_dhcp_ip = fct_scapy.listener_join(sniff_packet)
print (f"{Green}[+]{White} DHCP Server IP address is {legit_dhcp_ip}")

# dst mac why not ffffffff ?
# debian enable wifi promiscious mode