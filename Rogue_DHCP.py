#!/usr/bin/python3

# Import modules
import DHCP
import argparse

# Parse command
parser = argparse.ArgumentParser()
parser.add_argument("-i","--interface", required=True, help="Interface network")
args = parser.parse_args()

# Test DHCP Discover
#DHCP.discover("00:11:22:33:44:55", "00:11:22:33:44:55", args.interface)