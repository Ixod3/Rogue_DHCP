#!/usr/bin/python3

# Set color variables
Green = "\033[1;32m"
Blue = "\033[1;34m"
Red = "\033[1;33m"
White = "\033[0m"
Purple = "\033[1;35m"

# import module
import fct_arp
import fct_icmp
import fct_dhcp
import fct_interface
import scapy.all as scapy

def responder(sniff_packet, args, ip, mac, reserved_ip): # if IP is not set, it will be set to the IP of the interface
    if args.fake_host:
        # ARP Reply
        if sniff_packet[0].haslayer(scapy.ARP):
            # try
            try:
                mac_src = sniff_packet[0][scapy.ARP].hwsrc
                ip_dst = sniff_packet[0][scapy.ARP].pdst
                ip_src = sniff_packet[0][scapy.ARP].psrc
                print(f"[ARP] L'adresse IP {ip_src} recherche l'adresse IP {ip_dst}")
                fct_arp.reply(mac_src, ip_dst, ip_src, mac, args.interface)
            except:
                print ('pass')

        # ICMP Reply
        if sniff_packet[0].haslayer(scapy.ICMP):
            # try
            try:
                mac_src = sniff_packet[0][scapy.Ether].src
                mac_dst = sniff_packet[0][scapy.Ether].dst
                ip_src = sniff_packet[0][scapy.IP].src
                ip_dst = sniff_packet[0][scapy.IP].dst
                xid = sniff_packet[0][scapy.ICMP].id
                seq = sniff_packet[0][scapy.ICMP].seq
                payload = sniff_packet[0][scapy.ICMP].payload
                print(f"[ICMP] L'adresse IP {ip_src} requete l'adresse IP {ip_dst}")
                fct_icmp.reply(mac_src, mac_dst, ip_src, ip_dst, xid, seq, payload, args.interface)
            except:
                print ('pass 2')

    # DHCP offer
    if sniff_packet[0][scapy.DHCP].options[0][1] == 1 and sniff_packet[0][scapy.IP].src != fct_interface.get_informations_ip(args.interface):

        # Get DHCP Discover informations
        mac_dst = sniff_packet[0][scapy.Ether].src
        mac_src = fct_interface.get_mac(args.interface)
        ip_dst = sniff_packet[0][scapy.IP].src
        ip_src = ip
        xid = sniff_packet[0][scapy.BOOTP].xid

        for i in range(len(sniff_packet[0][scapy.DHCP].options)):
            if sniff_packet[0][scapy.DHCP].options[i][0] == 'hostname':
                hostname = sniff_packet[0][scapy.DHCP].options[i][1].decode('utf-8')

        if args.gateway:
            ip_gateway = args.gateway
        else:
            ip_gateway = fct_interface.get_informations_gateway(args.interface)

        if args.nameserver:
            ip_nameserver = args.nameserver
        else:
            ip_nameserver = fct_interface.get_informations_nameserver(args.interface)

        if args.domain:
            domain_name = args.domain
        else:
            domain_name = ""

        fct_dhcp.offer(mac_dst, reserved_ip[0][0], mac_src, ip_src, hostname, xid, fct_interface.get_informations_netmask(args.interface), ip_gateway, ip_nameserver, domain_name, 7200, reserved_ip[0][0], args.interface)
    
    # DHCP Ack
    if sniff_packet[0][scapy.DHCP].options[0][1] == 3 and sniff_packet[0][scapy.IP].src != fct_interface.get_informations_ip(args.interface):

        # Get DHCP Request informations
        mac_dst = sniff_packet[0][scapy.Ether].src
        mac_src = fct_interface.get_mac(args.interface)
        ip_dst = sniff_packet[0][scapy.IP].src
        ip_src = ip
        xid = sniff_packet[0][scapy.BOOTP].xid

        for i in range(len(sniff_packet[0][scapy.DHCP].options)):
            if sniff_packet[0][scapy.DHCP].options[i][0] == 'hostname':
                hostname = sniff_packet[0][scapy.DHCP].options[i][1].decode('utf-8')

        if args.gateway:
            ip_gateway = args.gateway
        else:
            ip_gateway = fct_interface.get_informations_gateway(args.interface)

        if args.nameserver:
            ip_nameserver = args.nameserver
        else:
            ip_nameserver = fct_interface.get_informations_nameserver(args.interface)

        if args.domain:
            domain_name = args.domain
        else:
            domain_name = ""

        print(f"{Purple}[DHCP]{White} Distributed IP Address - {reserved_ip[0][0]}")
        fct_dhcp.ack(mac_dst, reserved_ip[0][0], mac_src, ip_src, hostname, xid, fct_interface.get_informations_netmask(args.interface), ip_gateway, ip_nameserver, domain_name, 7200, reserved_ip[0][0], args.interface)

        # Remove reserved IP address from the list
        del reserved_ip[0]