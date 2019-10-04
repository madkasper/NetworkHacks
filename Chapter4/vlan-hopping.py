#!/usr/bin/python

from scapy.all import *

packet = Ether(dst="<dst-mac-address") ? / \
		 Dot1Q=(vlan=1) / \
		 Dot1Q=(vlan=2) / \
		 IP(dst="<dst-ip-address") / \
		 ICMP()

sendp(packet)