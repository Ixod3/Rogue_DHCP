#!/usr/bin/python3

# Import modules
import time
import subprocess
import sys

def get_mac(interface):
    ifconfig_return = subprocess.check_output(f"sudo ifconfig {interface}", shell=True, stderr=subprocess.STDOUT, text=True)
    actual_mac = ifconfig_return.split("ether ")[1]
    actual_mac = actual_mac.split(" ")[0]
    return actual_mac

def set_promiscuous(interface):
    subprocess.run(f"sudo ifconfig {interface} promisc 2>&1 > /dev/null", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    time.sleep(2)

def interface_information(interface):
    cmd_return = subprocess.check_output(f"ip a l {interface}", shell=True, stderr=subprocess.STDOUT, text=True)
    own_ip = cmd_return.split("inet ")[1]
    own_ip = own_ip.split(" brd")[0]
    cidr = int(own_ip.split("/")[1])
    own_ip = own_ip.split("/")[0]
    if cidr == 24:
        network_id = f"{own_ip.split('.')[0]}.{own_ip.split('.')[1]}.{own_ip.split('.')[2]}."
        host_number = 254
    else:
        print(f"[~] Network CIDR does not support")
        sys.exit()

    return  own_ip, network_id, host_number

