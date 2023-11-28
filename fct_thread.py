#!/usr/bin/python3

# import module
import fct_scapy
import fct_arp
import scapy.all as scapy
import threading
import time

# Stop all thread with ctrl+c
exit_event = threading.Event()

def fake_host(thread_id, fake_host_mac, interface):
    while True:
        # arp_listerner_start
        arp_listener = fct_scapy.listener_arp_start(f"192.168.1.14{thread_id+1}")
        # arp_listener join
        mac_src, ip_dst, ip_src = fct_scapy.listener_arp_join(arp_listener)
        print(f"L'adresse MAC source est {mac_src} est recherche l'adresse IP {ip_dst}")
        # arp how-has response
        fct_arp.response(mac_src, ip_dst, ip_src, fake_host_mac, interface)

#        # arp_listerner_start...
#        icmp_listener = fct_scapy.listener_start_icmp(f"192.168.1.14{thread_id+1}")
#        # arp_listerner_join...
#        ip_src, ip_dst = fct_scapy.listener_join_icmp(icmp_listener)
#        print(f"L'adress IP source de la requete ICMP est {ip_src} a destination de l'adresse IP 192.168.1.14{thread_id+1} ")

        # Stop all thread with ctrl+c
        if exit_event.is_set():
            break
    