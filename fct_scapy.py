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
    sniff_packet.join(timeout=0.2)
    if sniff_packet.results != None:
        result = sniff_packet.results
        mac_src = result[0][scapy.ARP].hwsrc
        ip_dst = result[0][scapy.ARP].pdst
        ip_src = result[0][scapy.ARP].psrc
        return mac_src, ip_dst, ip_src
    else: 
        mac_src = ""
        ip_dst = ""
        ip_src = ""
        return mac_src, ip_dst, ip_src

def listener_icmp_start(ip):
    sniff_packet = scapy.AsyncSniffer(count=1,filter=f"icmp[icmptype] == 8 and dst {ip}")
    sniff_packet.start()
    time.sleep(0.1)
    return sniff_packet

def listener_icmp_join(sniff_packet):
    sniff_packet.join(timeout=0.2)
    if sniff_packet.results != None:
        results = sniff_packet.results
        mac_src = results[0][scapy.Ether].src
        mac_dst = results[0][scapy.Ether].dst
        ip_src = results[0][scapy.IP].src
        ip_dst = results[0][scapy.IP].dst
        xid = results[0][scapy.ICMP].id
        seq = results[0][scapy.ICMP].seq
        payload = results[0][scapy.ICMP].payload
        return mac_src, mac_dst, ip_src, ip_dst, xid, seq, payload
    else: 
        mac_dst = ""
        mac_src = ""
        ip_dst = ""
        ip_src = ""
        xid = ""
        seq = ""
        payload = ""
        return mac_src, mac_dst, ip_src, ip_dst, xid, seq, payload