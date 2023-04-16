import socket
import struct
import hashlib
import pickle

def udp_send_data(ip, port ,data_list):
    address = (ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    version = 1
    pkt_type = 1
    seq_id = 1
    for x in data_list:
        #---header设计---
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

