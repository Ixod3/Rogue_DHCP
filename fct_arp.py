#!/usr/bin/python3

# Set color variables
Green = "\033[1;32m"
Blue = "\033[1;34m"
Red = "\033[1;33m"
White = "\033[0m"

# Import module
import scapy.all as scapy

def reply(mac_dst, ip_src, ip_dst, fake_host_mac, interface):
    arp_response = scapy.Ether(dst=mac_dst, src=fake_host_mac) / scapy.ARP(ptype=0x0800, op=2, pdst=ip_dst, hwdst=mac_dst, psrc=ip_src, hwsrc=fake_host_mac)
    scapy.sendp(arp_response, iface=interface, verbose=0)

def scan(network_id, host_number, interface):
    free_ip_list = []
    occuped_ip_list = []

    for i in range(host_number):
        free_ip_list.append(f"{network_id}{i+1}")

    for y in range(host_number):
        arp_req = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=f"{network_id}{y+1}", op=1)
        response = scapy.srp1(arp_req, verbose=0, timeout=0.3, iface=interface)
        if response:
            print(f"{Blue}[ARP]{White} IP Address {network_id}{y+1} already reserve")
            occuped_ip_list.append(f"{network_id}{y+1}")

    for z in range(len(occuped_ip_list)):
        free_ip_list.remove(occuped_ip_list[z])
 
    return free_ip_list, occuped_ip_list