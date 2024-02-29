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
        thread_responder = threading.Thread(target=fct_listener.listener(f"192.168.1.14{thread_id+1}", fake_host_mac, interface), args=())
        thread_responder.start()

        # Stop all thread with ctrl+c
        if exit_event.is_set():
            sys.exit()
        thread_responder.join()
