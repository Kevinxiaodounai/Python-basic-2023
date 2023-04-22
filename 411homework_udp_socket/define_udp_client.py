import socket
import struct
import hashlib
import pickle


def udp_send_data(ip, port, data_list):
    address = (ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # socket.AF_INET表示使用IPv4协议，而socket.SOCK_DGRAM表示使用UDP协议
    version = 1
    pkt_type = 1
    seq_id = 1
    for x in data_list:
        # ---header设计---
        # 2 字节 版本 1
        # 2 字节 类型 1 为请求 2 为响应（由于是UDP单向流量！所有此次试验只有请求）
        # 4 字节 ID号
        # 8 字节 长度

        # |  2  |    2   |    4    |        8        |
        # | ver |   type |    ID   |       len       |

        # ---变长数据部分---
        # 使用pickle转换数据

        # ---HASH校验---
        # 16字节 MD5值

        # 把Python数据或者对象Pickle成为二进制数据
        send_data = pickle.dumps(x)

        # 按照头部设计构建头部
        # H |    unsigned short  | integer | 2
        # L |    unsigned long   | integer | 4
        # Q | unsigned long long | integer | 8
        header = struct.pack('>HHLQ', version, pkt_type, seq_id, len(send_data))

        # 使用 头部+数据 产生MD5值
        m = hashlib.md5()
        m.update(header + send_data)
        md5_value = m.digest()
        # 直接产生二进制数据

        # 拼接 头部+发送数据+MD值， 然后返送到目的服务器
        s.sendto(header + send_data + md5_value, address)

        seq_id += 1
    s.close()


if __name__ == "__main__":
    from datetime import datetime

    user_data = ['乾颐堂', [1, 'qytang', 3], {'qytang': 1, 'test': 3}, {'datetime': datetime.now()}]
    udp_send_data('192.168.139.128', 6666, user_data)