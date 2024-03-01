#!/usr/bin/python3

# Import modules
import fct_dhcp
import fct_random
import fct_listener
import fct_interface
import fct_arp
import fct_thread
import argparse
import threading
import signal
import sys
import time

# Stop all thread with ctrl+c
def handler(signum, frame):
    global exit_event
    fct_thread.exit_event.set()
    exit(1)
 
signal.signal(signal.SIGINT, handler)

# Set color variables
Green = "\033[1;32m"
Blue = "\033[1;34m"
Red = "\033[1;33m"
White = "\033[0m"

# Parse command
parser = argparse.ArgumentParser()
parser.add_argument("-I","--interface", required=True, help="Interface network")
parser.add_argument("-PR","--ping_arp", action='store_true', help="enable ARP Scan")
parser.add_argument("-FH","--fake_host", action='store_true', help="enable FakeHost (ARP/ICMP response)")
parser.add_argument("-N","--nameserver", action='store', help="Include fake DNS server inside DHCP configuration")
parser.add_argument("-G","--gateway", action='store', help="Include fake gateway inside DHCP configuration")
parser.add_argument("-D","--domain", action='store', help="Include fake domain inside DHCP configuration")
args = parser.parse_args()

# Enable promisc mode 
fct_interface.set_promiscuous(args.interface)

# scan ARP
if (args.ping_arp):
    own_ip, network_id, host_number = fct_interface.get_informations(args.interface)
    free_ip, occuped_ip = fct_arp.scan(network_id, host_number, args.interface)
else:
    own_ip, network_id, host_number = fct_interface.get_informations(args.interface)
    free_ip = []
    occuped_ip = []
    for i in range(host_number):
        free_ip.append(f"{network_id}{i+1}")

# listener
fct_listener.listener(free_ip, occuped_ip, args)