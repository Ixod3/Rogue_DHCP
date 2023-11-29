#!/usr/bin/python3

# Import modules
import scapy.all as scapy

def reply(mac_dst, mac_src, ip_dst, ip_src, xid, seq, payload, interface):
    icmp_reply = scapy.Ether(src=mac_src, dst=mac_dst) / scapy.IP(src=ip_src, dst=ip_dst) / scapy.ICMP(type=0, code=0, id=xid, seq=seq) / payload
    scapy.sendp(icmp_reply, iface=interface, verbose=0)