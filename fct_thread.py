#!/usr/bin/python3

# import module
import scapy.all as scapy
import threading
import time

# Stop all thread with ctrl+c
exit_event = threading.Event()

def fake_host(thread_id):
    for i in range(5):
        print(f"Hello from {thread_id}")
        time.sleep(3)
        # Stop all thread with ctrl+c
        if exit_event.is_set():
            break
    