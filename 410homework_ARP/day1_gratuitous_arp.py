import logging

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  # 清除报错
from kamene.all import *
from /tools/get_mac_netifaces import get_mac_address


def gratuituous_arp(ipaddress, ifname):
    localmac = get_mac_address(ifname)
    gratuituous_arp.pkt = Ether(src=localmac,
                                dst='ff:ff:ff:ff:ff:ff')/ARP(op=2,
                                                             hwsrc=localmac,
                                                             hwdst=localmac,
                                                             psrc=ip_address,
                                                             pdst=ip_address)
    sendp(gratuitous_arp_pkt ,iface=scapy_iface(ifname), verbos=False)

if __name__ == "__main__":
    gratuitous_arp('10.1.1.1', ifname='ens160')

