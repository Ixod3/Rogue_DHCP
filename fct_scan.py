#!/usr/bin/python3

# Import modules
import scapy.all as scapy

def arp(ip_src, ip_dst, interface):
    arp_req = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst=ip_dst, op=1)
    response = scapy.srp1(arp_req, verbose=0, timeout=0.3, iface=interface)
    if response:
        check = True
    else:
        check = False
    return check