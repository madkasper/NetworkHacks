#!/usr/bin/python
#
# For details see www.securityfriday.com/promiscous_detection_01.pdf
#
import sys
from scapy.all import promiscping

if len(sys.argv) < 2:
	print sys.argv[0] + " <net>"
	sys.exit()

promiscping(sys.argv[1])