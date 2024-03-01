#!/usr/bin/python3

# Set color variables
Green = "\033[1;32m"
Blue = "\033[1;34m"
White = "\033[0m"

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
    print(f"{Blue}[PROMISC]{White} Set interface {interface} to promiscuous mode")
    subprocess.run(f"sudo ifconfig {interface} promisc 2>&1 > /dev/null", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    time.sleep(2)

def get_informations(interface):
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

def get_informations_ip(interface):
    cmd_return = subprocess.check_output(f"ip a l {interface}", shell=True, stderr=subprocess.STDOUT, text=True)
    own_ip = cmd_return.split("inet ")[1]
    own_ip = own_ip.split(" brd")[0]
    own_ip = own_ip.split("/")[0]

    return  own_ip

def get_informations_netmask(interface):
    cmd_return = subprocess.check_output(f"ifconfig {interface}", shell=True, stderr=subprocess.STDOUT, text=True)
    own_netmask = cmd_return.split("netmask ")[1]
    own_netmask = own_netmask.split(" broadcast")[0]

    return  own_netmask

def get_informations_gateway(interface):
    cmd_return = subprocess.check_output("ip route show | grep default | awk '{print $3}'", shell=True, stderr=subprocess.STDOUT, text=True)

    return cmd_return

def get_informations_nameserver(interface):
    cmd_return = subprocess.check_output("cat /etc/resolv.conf | grep nameserver | awk '{print $2}'", shell=True, stderr=subprocess.STDOUT, text=True)
    own_nameserver = cmd_return.split("\n")[0]

    return own_nameserver