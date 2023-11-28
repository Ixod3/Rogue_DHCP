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

def listener_arp_start(ip):
    sniff_packet = scapy.AsyncSniffer(count=1,filter=f"arp and arp[6:2] = 1 and host {ip}")
    sniff_packet.start()
    time.sleep(0.1)
    return sniff_packet

def listener_arp_join(sniff_packet):
    sniff_packet.join()
    request = sniff_packet.results
    mac_src = request[0][scapy.ARP].hwsrc
    ip_dst = request[0][scapy.ARP].pdst
    ip_src = request[0][scapy.ARP].psrc
    return mac_src, ip_dst, ip_src

#def listener_icmp_start(ip):
#    sniff_packet = scapy.AsyncSniffer(count=1,filter=f"icmp and dst Ether")
#    sniff_packet.start()
#    time.sleep(0.1)
#    return sniff_packet
#
#def listener_icmp_join(sniff_packet):
#    sniff_packet.join()
#    request = sniff_packet.results
#    ip_src = request[0][scapy.IP].src
#    ip_dst = request[0][scapy.IP].dst
#    return ip_src, ip_dst