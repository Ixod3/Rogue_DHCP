#!/usr/bin/python3

# Import modules
import scapy.all as scapy
import time

def listener_start(src_mac):
    sniff_packet = scapy.AsyncSniffer(count=1,filter=f"udp and src port 67 and dst port 68 and ether dst {src_mac}", timeout=5)
    sniff_packet.start()
    time.sleep(0.1)
    return sniff_packet

def listener_join(sniff_packet):
    sniff_packet.join()
    dhcp_offer = sniff_packet.results
    return dhcp_offer

def listener_start_icmp(ip):
    sniff_packet = scapy.AsyncSniffer(count=1,filter=f"icmp and dst host {ip}")
    sniff_packet.start()
    time.sleep(0.1)
    return sniff_packet

def listener_join_icmp(sniff_packet):
    sniff_packet.join()
    request = sniff_packet.results
    ip_src = request[0][scapy.IP].src
    return ip_src