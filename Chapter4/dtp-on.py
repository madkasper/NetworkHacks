#!/usr/bin/python

# Send dynamic-desirable-packet to Cisco
# switch to enable VLAN trunc-port (DTP).
#
# Acess VLAN: 
#
# $ vconfig add eth0 <vlan-id>
# $ ifconfig eth0.<vlan-id> <ip_from_vlan_range> up
#

import sys
from scapy.layers.12 import Dot3, LLC, SNAP
from scapy.contrib.dtp import *

if len(sys.argv) < 2:
	print sys.argv[0] + " <dev>"
	sys.exit(1)

negotiate_trunk(iface=sys.argv[1])