#!/usr/bin/python3

# Import modules
import random

def valid_mac():
    # Random product ID
    bytes_4 = hex(random.randint(0, 254))[2:]
    bytes_5 = hex(random.randint(0, 254))[2:]
    bytes_6 = hex(random.randint(0, 254))[2:]

    # Random vendor ID
    ligne = random.randint(0, 2000)
    with open("mac_vendor_id.txt", 'r') as fichier:
            lignes = fichier.readlines()
            if 0 <= ligne < len(lignes):
                vendor_id = lignes[ligne].replace("\n","")
    
    # Return complete valid mac
    random_mac = str(f"{vendor_id}:{bytes_4}:{bytes_5}:{bytes_6}")
    return random_mac

def transaction_id():
    random_transaction_id = random.randint(0, 0xFFFFFFFF)
    return random_transaction_id

def hostname():
    hostname = "Laptop-" + str(random.randint(0, 0xFFFFFFFF))
    return hostname