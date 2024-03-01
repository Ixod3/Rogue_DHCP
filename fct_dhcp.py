#!/usr/bin/python3

# Import modules
import scapy.all as scapy
import time

# Set color variables
Green = "\033[1;32m"
Blue = "\033[1;34m"
White = "\033[0m"

# DHCP Discover
def discover(mac_broadcast, ip_broadcast, mac_client, ip_client, hostname, xid, args):

    # Couche réseau
    ethernet = scapy.Ether(dst=mac_broadcast, src=mac_client)
    ip = scapy.IP(src=ip_client, dst=ip_broadcast)
    udp = scapy.UDP(sport=68, dport=67)
    bootp = scapy.BOOTP(chaddr=(int(mac_client.replace(":", ""), 16).to_bytes(6, "big")), xid=xid, flags=0x0000)
    dhcp = scapy.DHCP(options=[('message-type', 'discover'), ('client_id', mac_client), ('param_req_list',[1,2,3,6,12,15,17,26,28,33,40,41,42,119,121,249,252]), ("max_dhcp_size", 576), ('hostname', hostname), "end"])

    # Assemblage + Envoie de la requête
    packet = ethernet/ip/udp/bootp/dhcp
    scapy.sendp(packet, iface=args.interface, verbose=0)


# DHCP Offer
def offer(mac_client, ip_broadcast, mac_server, ip_client, hostname, xid, subnet_mask, ip_router, ip_nameserver, domain_name, lease_time, ip_offer, interface):
    
    time.sleep(1)
    # Couche réseau
    ethernet = scapy.Ether(dst=mac_client, src=mac_server)
    ip = scapy.IP(src=ip_client, dst=ip_broadcast)
    udp = scapy.UDP(sport=67, dport=68)
    bootp = scapy.BOOTP(op=2, chaddr=(int(mac_client.replace(":", ""), 16).to_bytes(6, "big")), yiaddr=ip_offer, xid=xid, flags=0x0000)
    dhcp = scapy.DHCP(options=[('message-type', 'offer'), ("subnet_mask", subnet_mask), ("router", ip_router), ("name_server", ip_nameserver), ("domain", domain_name), ("lease_time", lease_time), ('client_id', mac_client), ('hostname', hostname), "end"])

    # Assemblage + Envoie de la requête
    packet = ethernet/ip/udp/bootp/dhcp
    scapy.sendp(packet, iface=interface, verbose=0)


# DHCP Request
def request(mac_broadcast, ip_broadcast, mac_client, ip_client, hostname, xid, ip_dhcp_server, ip_request, args):

    # Couche réseau
    ethernet = scapy.Ether(dst=mac_broadcast, src=mac_client)
    ip = scapy.IP(src=ip_client, dst=ip_broadcast)
    udp = scapy.UDP(sport=68, dport=67)
    bootp = scapy.BOOTP(chaddr=(int(mac_client.replace(":", ""), 16).to_bytes(6, "big")), xid=xid, flags=0x0000)
    dhcp = scapy.DHCP(options=[('message-type', 'request'), ("requested_addr", ip_request), ("server_id", ip_dhcp_server), ('param_req_list',[1,2,3,6,12,15,17,26,28,33,40,41,42,119,121,249,252]), ("max_dhcp_size", 576), ('client_id', mac_client), ('hostname', hostname), "end"])

    # Assemblage + Envoie de la requête
    packet = ethernet/ip/udp/bootp/dhcp
    scapy.sendp(packet, iface=args.interface, verbose=0)


# DHCP Ack
def ack(mac_client, ip_broadcast, mac_server, ip_client, hostname, xid, subnet_mask, ip_router, ip_nameserver, domain_name, lease_time, ip_offer, interface):
    
    time.sleep(1)
    # Couche réseau
    ethernet = scapy.Ether(dst=mac_client, src=mac_server)
    ip = scapy.IP(src=ip_client, dst=ip_broadcast)
    udp = scapy.UDP(sport=67, dport=68)
    bootp = scapy.BOOTP(op=2, chaddr=(int(mac_client.replace(":", ""), 16).to_bytes(6, "big")), yiaddr=ip_offer, xid=xid, flags=0x0000)
    dhcp = scapy.DHCP(options=[('message-type', 'ack'), ("subnet_mask", subnet_mask), ("router", ip_router), ("name_server", ip_nameserver), ("domain", domain_name), ("lease_time", lease_time), ('client_id', mac_client), ('hostname', hostname), "end"])

    # Assemblage + Envoie de la requête
    packet = ethernet/ip/udp/bootp/dhcp
    scapy.sendp(packet, iface=interface, verbose=0)

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