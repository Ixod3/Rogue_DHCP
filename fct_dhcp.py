#!/usr/bin/python3

# Import modules
import scapy.all as scapy
import time

# Set color variables
Green = "\033[1;32m"
Blue = "\033[1;34m"
White = "\033[0m"

# DHCP Discover
def discover(src_mac, hostname, xid, interface):
    src_mac_bytes = (int(src_mac.replace(":", ""), 16).to_bytes(6, "big"))
    dhcp_discover = scapy.Ether(src=src_mac,dst="ff:ff:ff:ff:ff:ff") / scapy.IP(src="0.0.0.0", dst="255.255.255.255") / scapy.UDP(sport=68, dport=67) / scapy.BOOTP(chaddr=src_mac_bytes, xid=xid, flags=0x0000) / scapy.DHCP(options=[("message-type", "discover"), ('client_id', src_mac), ('param_req_list',[1,2,3,6,12,15,26,28,33,40,41,42,119,121]),('hostname', hostname), "end"])
    scapy.sendp(dhcp_discover, iface=interface, verbose=0)
    
# DHCP Offer
def offer():
    print('pass')

# DHCP Request
def request(src_mac, request_ip, hostname, xid, interface):
    src_mac_bytes = (int(src_mac.replace(":", ""), 16).to_bytes(6, "big"))
    dhcp_request = scapy.Ether(src=src_mac,dst="ff:ff:ff:ff:ff:ff") / scapy.IP(src="0.0.0.0", dst="255.255.255.255") / scapy.UDP(sport=68, dport=67) / scapy.BOOTP(op=1, ciaddr="0.0.0.0", chaddr=src_mac_bytes, xid=xid) / scapy.DHCP(options=[('message-type', 'request'), ("client_id", b'\x01' + src_mac_bytes), ("param_req_list", (1), (2), (6), (12), (15), (26), (28), (121), (3), (33), (40), (41), (42), (119), (249), (252), (17)), ("max_dhcp_size", 1500), ("requested_addr", request_ip), ('hostname', hostname), 'end'])
    scapy.sendp(dhcp_request, iface=interface, verbose=0)

# DHCP Ack
def ack():
    print('pass')

# Get DHCP Offer information
def get_offer_information(dhcp_offer):
    offer_ip = dhcp_offer[0][scapy.BOOTP].yiaddr
    offer_mac = dhcp_offer[0][scapy.Ether].dst
    return offer_mac, offer_ip

# Get DHCP Ack information
def get_ack_information(dhcp_ack):
    ack_ip = dhcp_ack[0][scapy.BOOTP].yiaddr
    ack_mac = dhcp_ack[0][scapy.Ether].dst
    return ack_mac, ack_ip

def listener(mac):
    sniff_packet = scapy.AsyncSniffer(count=1, filter=f"udp and src port 67 and dst port 68 and ether dst {mac}", timeout=3)
    sniff_packet.start()
    time.sleep(0.1)
    return sniff_packet

def listener_join(sniff_packet):
    sniff_packet.join()
    dhcp_offer = sniff_packet.results
    return dhcp_offer