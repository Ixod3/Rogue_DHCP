# Rogue_DHCP

## Prerequis

Scapy

```bash
sudo pip3 install scapy
```

Macchanger

```bash
apt install macchanger -y
```

Sources : 
- https://github.com/secdev/scapy/blob/master/scapy/layers/dhcp.py

## Next

- Block auto DHCP request with filter on transaction ID ?
- Implement DHCP Request
- Detect free ip with ARP and ICMP request
- Renew reserved ip before expire (wire connexion only)
- DHCP Release for reserve IP already reserved ?
