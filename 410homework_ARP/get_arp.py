
import logging

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  # 清除报错
from kamene.all import *


def arp_request(ip_address):
    try:  # 发送ARP请求并等待响应
        result_raw = sr1(ARP(pdst=ip_address),
                         timeout=1,
                         verbose=False)
        return ip_address, result_raw.getlayer(ARP).fields.get('hwsrc')

    except AttributeError:
        return ip_address, None


if __name__ == "__main__":
    # Windows Linux均可使用
    arp_result = arp_request('172.16.158.129')
    print("IP地址:", arp_result[0], "MAC地址:", arp_result[1])
