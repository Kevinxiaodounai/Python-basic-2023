import socket
import struct
import hashlib
import sys
import pickle

# 绑定地址到udp端口

address = ('0.0.0.0', 6666)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# socket.AF_INET表示使用IPv4协议，而socket.SOCK_DGRAM表示使用UDP协议
s.bind(address)

print('UDP服务器就绪！等待客户数据！')
while True:
    try:
        # 接受数据[注意： 此处限制了发送大小为512]
        recv_source_date = s.recvfrom(512)

        # 提取发送数据与socket信息 （源地址， 源端口）
        rdata, addr = recv_source_date

        # 截取前16个字节的头部
        header = rdata[:16]

        # 按照头部设计解封装到 版本， 类型， 序列号， 长度
        uppack_header = struct.unpack('>HHLQ', header)
        version = uppack_header[0]
        pkt_type = uppack_header[1]
        seq_id = uppack_header[2]
        length = uppack_header[3]

        # 切掉头部数据， 得到后续数据（包含数据+MD5值）
        rdata = rdata[16:]

        # 按照数据长， 切出数据
        data = rdata[:length]

        # 切掉数据， 剩余的为MD5值
        md5_recv = rdata[length:]

        # 把收到的 头部+数据 计算MD5值
        m = hashlib.md5()
        m.update(header + data)
        md5_value = m.digest()

        # 如果本地计算的MD5值等于发送过来的MD5值
        if md5_recv == md5_value:
            print('=' * 80)
            print("{0:<30}:{1:<30}".format("数据源自于", str(addr)))
            print("{0:<30}:{1:<30}".format("数据序列号", seq_id))
            print("{0:<30}:{1:<30}".format("数据长度为", length))
            print("{0:<30}:{1:<30}".format("数据内容为", str(pickle.loads(data))))
        else:
            print('MD5校验错误！')
    except KeyboardInterrupt:
        sys.exit()
