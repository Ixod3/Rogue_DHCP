# Rogue_DHCP

## Description

Python script for Rogue DHCP attack (DNS poisoning, gateway spoofing, etc.) with DHCP Starvation and Fake Host functionality for responds to ARP and ICMP requests from clients

**Disclaimer:**
This script is intended for educational purposes only. Do not use it for malicious activities. It can cause serious disruptions to a network and may lead to legal consequences. I am not responsible for its use.

## Requirements

```sh
# Install
sudo apt install net-tools
sudo pip3 install scapy

# Check
sudo ifconfig
pip3 show scapy
```

## Installation

```sh
git clone https://github.com/Ixod3/Rogue_DHCP.git
cd Rogue_DHCP
```

## Usage

```sh
# Fake Hosts with Rogue DNS server example
sudo ./Rogue_DHCP.py -I eth0 -FH -N 192.168.1.33

# Rogue Gateway without fake hosts example
sudo ./Rogue_DHCP.py -I eth0 -G 192.168.1.33
```

show more options with `-h` or `--help`

## Details

### License

[GNU General Public License (GPL) v3](https://www.gnu.org/licenses/gpl-3.0.html)

### Source
- https://github.com/secdev/scapy/blob/master/scapy/layers/dhcp.py