#!/usr/bin/python3

# Import modules
import DHCP
import Random
import argparse

# Parse command
parser = argparse.ArgumentParser()
parser.add_argument("-i","--interface", required=True, help="Interface network")
args = parser.parse_args()

# Test DHCP Discover
xid = Random.rand_transaction_id()
DHCP.discover("44:af:28:d9:46:a3", xid, args.interface)

# dst mac why not ffffffff ?
# debian enable wifi promiscious mode