#!/usr/bin/python3

# Import modules
import time
import subprocess

def get_mac(interface):
    ifconfig_return = subprocess.check_output(f"sudo ifconfig {interface}", shell=True, stderr=subprocess.STDOUT, text=True)
    actual_mac = ifconfig_return.split("ether ")[1]
    actual_mac = actual_mac.split(" ")[0]
    return actual_mac

def set_promiscuous(interface):
    subprocess.run(f"sudo ifconfig {interface} promisc 2>&1 > /dev/null", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    time.sleep(3)