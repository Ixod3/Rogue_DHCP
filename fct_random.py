#!/usr/bin/python3

# Import modules
import random

def valid_mac_2():
    bytes_4 = hex(random.randint(0, 254))[2:]
    bytes_5 = hex(random.randint(0, 254))[2:]
    bytes_6 = hex(random.randint(0, 254))[2:]
    random_mac = str(f"fc:3c:2c:{bytes_4}:{bytes_5}:{bytes_6}")

def transaction_id():
    random_transaction_id = random.randint(0, 0xFFFFFFF)
    return random_transaction_id

def valid_mac():
    return "44:af:28:d9:46:a2"
    #return "2c:6d:c1:ab:6e:f9"