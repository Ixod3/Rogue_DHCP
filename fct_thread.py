#!/usr/bin/python3

# import module
import scapy.all as scapy
import time

def fake_host(thread_id):
    for i in range(3):
        print(f"Hello from {thread_id}")
        time.sleep(3)