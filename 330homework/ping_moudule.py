import logging
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)


from kamene.all import *
def qping(ip):
    pkt = IP(dst=ip) / ICMP()
    response = sr1(pkt, timeout=1, verbose=False)
    if response :
        print(f'{ip:^10}通')
        return ip,True
    else:
        print(f'{ip:^10}不通')

if __name__=='__main__':
    result=qping('192.168.31.1')
