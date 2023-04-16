import logging

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  # 清除报错
from kamene.all import *

from get_mac_netifaces import get_mac_address
from scapy_iface import scapy_iface

def gratuituous_arp(ip_address, ifname):
    localmac = get_mac_address(ifname)
    gratuitous_arp_pkt = Ether(src=localmac,
                                dst='ff:ff:ff:ff:ff:ff')/ARP(op=2,
                                                             hwsrc=localmac,
                                                             hwdst=localmac,
                                                             psrc=ip_address,
                                                             pdst=ip_address)
    sendp(gratuitous_arp_pkt ,iface=scapy_iface(ifname), verbose=False)

if __name__ == "__main__":
    gratuituous_arp('10.1.1.1', ifname='ens160')

