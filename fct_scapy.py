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
    #legit_dhcp_ip = results[0][scapy.IP].src
    #legit_dhcp_mac = results[0][scapy.Ether].src
    return dhcp_offer