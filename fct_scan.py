#!/usr/bin/python3

# Set color variables
Green = "\033[1;32m"
Blue = "\033[1;34m"
Red = "\033[1;33m"
White = "\033[0m"

# Import modules
import scapy.all as scapy

def arp(network_id, host_number, interface):
    free_ip_list = []
    occuped_ip_list = []

    for i in range(host_number):
        free_ip_list.append(f"{network_id}{i+1}")

    for y in range(host_number):
        arp_req = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=f"{network_id}{y+1}", op=1)
        response = scapy.srp1(arp_req, verbose=0, timeout=0.3, iface=interface)
        if response:
            print(f"{Green}[+]{White} IP Address {network_id}{y+1} is used")
            occuped_ip_list.append(f"{network_id}{y+1}")

    for z in range(len(occuped_ip_list)):
        free_ip_list.remove(occuped_ip_list[z])
 
    return free_ip_list