#!/usr/bin/python3

# Import modules
import time
import subprocess

def change_mac(interface):
    subprocess.run(f"sudo ifconfig {interface} down 2>&1 > /dev/null", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    subprocess.run(f"sudo dhclient -r 2>&1 > /dev/null", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    subprocess.run(f"sudo macchanger -r {interface} 2>&1 > /dev/null", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    subprocess.run(f"sudo ifconfig {interface} up 2>&1 > /dev/null", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    time.sleep(3)

def get_mac(interface):
    ifconfig_return = subprocess.check_output(f"sudo ifconfig {interface}", shell=True, stderr=subprocess.STDOUT, text=True)
    actual_mac = ifconfig_return.split("ether ")[1]
    actual_mac = actual_mac.split(" ")[0]
    return actual_mac

def set_promiscuous(interface):
    subprocess.run(f"sudo ifconfig {interface} up 2>&1 > /dev/null", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    time.sleep(3)