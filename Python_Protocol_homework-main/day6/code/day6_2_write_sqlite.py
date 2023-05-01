#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# 在Linux使用crond调度运行, 需要添加项目主目录到搜索路径
import sys
sys.path.extend(['/python_homework_protocol/'])

from sqlalchemy.orm import sessionmaker
from day6_1_create_db import InternfaceMonitor, engine
from snmpv2_getall import snmpv2_getall


Session = sessionmaker(bind=engine)
session = Session()

# 设备IP地址列表
ip_list = ['10.1.1.1', '10.1.1.2']


# 获取设备CPU和内存信息, 并写入数据
def get_info_writedb(ip_list, rocommunity):
    router_info_list = []
    for device_ip in ip_list:
        try:
            # 通过SNMP获取设备的所有信息
            get_all = snmpv2_getall(device_ip, rocommunity)
            # 提取采集的接口列表
            interface_list = get_all.get('if_list')

            for interface in interface_list:
                interface_name = interface.get('name')
                in_bytes = interface.get('in_bytes')
                out_bytes = interface.get('out_bytes')

                interface_info = InternfaceMonitor(device_ip=device_ip,
                                                   interface_name=interface_name,
                                                   in_bytes=in_bytes,
                                                   out_bytes=out_bytes)
                print(interface_info)
                router_info_list.append(interface_info)

        except Exception as e:
            print(e)
            pass

    # 写入数据库并提交
    print(router_info_list)
    session.add_all(router_info_list)
    session.commit()


if __name__ == '__main__':
    get_info_writedb(ip_list, 'qytangro')
