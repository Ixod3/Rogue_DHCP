#!/usr/bin/python3

# import module
import fct_listener
import fct_arp
import fct_icmp
import scapy.all as scapy
import threading
import time
import sys

# Stop all thread with ctrl+c
exit_event = threading.Event()

def fake_host(thread_id, fake_host_mac, interface):
    while True:
        # arp_listerner_start
#        arp_listener = fct_scapy.listener_arp_start(f"192.168.1.14{thread_id+1}", fake_host_mac, interface)
        thread_responder = threading.Thread(target=fct_listener.listener(f"192.168.1.14{thread_id+1}", fake_host_mac, interface), args=())
        thread_responder.start()
#        # arp_listener join
#        mac_src, ip_dst, ip_src = fct_scapy.listener_arp_join(arp_listener)
#        # arp response
#        if mac_src != "" and ip_dst != "" and  ip_src != "":
#            print(f"[ARP] L'adresse MAC source est {mac_src} est recherche l'adresse IP {ip_dst}")
#            fct_arp.response(mac_src, ip_dst, ip_src, fake_host_mac, interface)

        #thread_icmp = threading.Thread(target=fct_scapy.icmp_responder(f"192.168.1.14{thread_id+1}", interface), args=())
        #thread_icmp.start()
        # icmp_listener_start
#        icmp_listener = fct_scapy.listener_icmp_start(f"192.168.1.14{thread_id+1}")
#        # icmp_listener join
#        mac_src, mac_dst, ip_src, ip_dst, xid, seq, payload = fct_scapy.listener_icmp_join(icmp_listener)
#        # icmp reply
#        if ip_dst != "" and  ip_src != "":
#            print(f"[ICMP] L'adress IP source est {ip_src} a destination de l'IP 192.168.1.14{thread_id+1}")
#            fct_icmp.reply(mac_src, mac_dst, ip_src, ip_dst, xid, seq, payload, interface)

        # liberation de l'espace memoire
        #del arp_listener, mac_src, ip_dst, ip_src, icmp_listener, mac_dst, xid, seq, payload

        # Stop all thread with ctrl+c
        if exit_event.is_set():
            sys.exit()
        thread_responder.join()
