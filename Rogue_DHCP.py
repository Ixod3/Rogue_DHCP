#!/usr/bin/python3

# Import modules
import fct_dhcp
import fct_random
import fct_scapy
import fct_os
import fct_scan
import argparse
import sys
import time

# Set color variables
Green = "\033[1;32m"
Blue = "\033[1;34m"
Red = "\033[1;33m"
White = "\033[0m"

# Parse command
parser = argparse.ArgumentParser()
parser.add_argument("-i","--interface", required=True, help="Interface network")
args = parser.parse_args()

# scan ARP
own_ip, network_id, host_number = fct_os.interface_ip(args.interface)

for i in range(host_number):
    result = fct_scan.arp(own_ip, f"{network_id}{i+1}", args.interface)
    if result == True:
        print(f"{Green}[+]{White} IP Address {network_id}{i+1} is used")

# Enable promisc mode
print(f"{Blue}[~]{White} Enable promisc mode on {args.interface}")
fct_os.set_promiscuous(args.interface)
# Get interface's mac
random_mac = fct_random.valid_mac()
# Get random hostname
hostname = fct_random.hostname()
# Get random transaction ID
xid = fct_random.transaction_id()

# Listener discover start
sniff_packet = fct_scapy.listener_start(random_mac)
# DHCP Discover
fct_dhcp.discover(random_mac, hostname, xid, args.interface)
# Listener discover join
dhcp_offer = fct_scapy.listener_join(sniff_packet)
print (f"{Green}[+]{White} Capture - DHCP Offer")
# Get DHCP offer information
dst_mac, offer_ip = fct_dhcp.get_offer_information(dhcp_offer)

# Listener request start
sniff_packet = fct_scapy.listener_start(dst_mac)
# DHCP request
fct_dhcp.request(dst_mac, offer_ip, hostname, xid, args.interface)
# Listener request join
dhcp_ack = fct_scapy.listener_join(sniff_packet)
print (f"{Green}[+]{White} Capture - DHCP ACK")
# Get DHCP ACK information
dst_mac, ack_ip = fct_dhcp.get_ack_information(dhcp_ack)