import logging
logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
# 创建一个ping的系统
from scapy.all import *


class QQPING:
    def __init__(self, ip):
        self.ip = ip
        self.src_ip = ''
        self.length = 100

    def make_pkt(self):
        if self.src_ip:
            self.pkt = IP(dst=self.ip, src=self.src_ip)
            ICMP() / (b'g' * self.length)
        else:
            self.pkt = IP(dst=self.ip) / ICMP() / (b'g' * self.length)

    def one(self):
        self.make_pkt()
        result = sr1(self.pkt, timeout=1, verbose=False)
        if result:
            print(self.ip, '可达')
        else:
            print(self.ip, '不可达')

    def ping(self):
        self.make_pkt()
        for i in range (5):
            result = sr1(self.pkt, timeout=1, verbose=False)
            if result:
                print('!', end='',flush=True)
            else:
                print('.', end='',flush=True)
        print()

    def __str__(self):
        if not self.src_ip:
            return '<{0}=>dstip: {1}, size:{2}>'.format(self.__class__.__name__, self.ip, self.length)
        else:
            return '<{0}=>srcip: {1}, dstip:{2},size:{3}>'.format(self.__class__.__name__, self.src_ip, self.ip, self.length)


class NewPing(QQPING):
    def ping(self):
        self.make_pkt()
        for i in range (5):
            result = sr1(self.pkt, timeout=1, verbose=False)
            if result:
                print('!', end='',flush=True)
            else:
                print('.', end='',flush=True)
        print()


if __name__ == '__main__':
    ping = QQPING('192.168.31.1')
    total_len = 70


    def print_new(word, s='-'):
        print('{0}{1}{2}'.format(s * int((70 - len(word)) / 2), word, s * int((70 - len(word)) / 2)))
    print_new('print class')
    print(ping)
    print_new('ping one for sure reachable')
    ping.one()
    print_new('ping five')
    ping.ping()
    print_new('set payload length')
    ping.length=200
    print(ping)
    ping.ping()
    print_new('set ping src ip address')
    ping.src_ip = '192.168.1.123'
    print(ping)
    ping.ping()
    print_new('new class NewPing', '=')
    newping = NewPing('192.168.1.1')
    newping.length = 300
    print(newping)
    newping.ping()
