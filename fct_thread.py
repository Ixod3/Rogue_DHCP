#!/usr/bin/python3

# import module
import fct_scapy
import scapy.all as scapy
import threading
import time


# Stop all thread with ctrl+c
exit_event = threading.Event()

def fake_host(thread_id):
    while True:
        icmp_listener = fct_scapy.listener_start_icmp(f"192.168.1.14{thread_id+1}")
        ip_src = fct_scapy.listener_join_icmp(icmp_listener)
        print(f"L'adress IP source de la requete ICMP est {ip_src} a destination de l'adresse IP 192.168.1.14{thread_id+1} ")
        # Stop all thread with ctrl+c
        if exit_event.is_set():
            break
    