#!/usr/bin/python3

# import module
import fct_arp
import fct_icmp
import scapy.all as scapy

def responder(sniff_packet, fake_host_mac, interface):
    # ARP Reply
    if sniff_packet[0].haslayer(scapy.ARP):
        # try
        try:
            mac_src = sniff_packet[0][scapy.ARP].hwsrc
            ip_dst = sniff_packet[0][scapy.ARP].pdst
            ip_src = sniff_packet[0][scapy.ARP].psrc
            print(f"[ARP] L'adresse IP {ip_src} recherche l'adresse IP {ip_dst}")
            fct_arp.reply(mac_src, ip_dst, ip_src, fake_host_mac, interface)
        except:
            print ('pass')

    # ICMP Reply
    if sniff_packet[0].haslayer(scapy.ICMP):
        # try
        try:
            mac_src = sniff_packet[0][scapy.Ether].src
            mac_dst = sniff_packet[0][scapy.Ether].dst
            ip_src = sniff_packet[0][scapy.IP].src
            ip_dst = sniff_packet[0][scapy.IP].dst
            xid = sniff_packet[0][scapy.ICMP].id
            seq = sniff_packet[0][scapy.ICMP].seq
            payload = sniff_packet[0][scapy.ICMP].payload
            print(f"[ICMP] L'adresse IP {ip_src} requete l'adresse IP {ip_dst}")
            fct_icmp.reply(mac_src, mac_dst, ip_src, ip_dst, xid, seq, payload, interface)
        except:
            print ('pass 2')