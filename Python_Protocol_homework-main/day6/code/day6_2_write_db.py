#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# 在Linux使用crond调度运行, 需要添加项目主目录到搜索路径
import sys
sys.path.extend(['/python_homework_protocol/'])

from sqlalchemy.orm import sessionmaker
from new_homework.day6.code.day6_1_create_db import InternfaceMonitor, engine
from new_homework.day4.code.tools.day4_snmp_get_all import snmpv2_getall


Session = sessionmaker(bind=engine)
session = Session()

# 设备IP地址列表
ip_list = ['10.1.1.1', '10.1.1.2']


# 获取设备CPU和内存信息, 并写入数据
def get_info_writedb(ip_list, rocommunity):
    router_info_list = []
    for ip in ip_list:
        # 通过SNMP获取设备的所有信息, CPU, MEM和接口
        try:
            get_all = snmpv2_getall(ip, rocommunity)

            interface_list = get_all.get('if_list')

            for interface in interface_list:
                interface_info = InternfaceMonitor(device_ip=get_all.get('ip'),
                                                   interface_name=interface.get('name'),
                                                   in_bytes=interface.get('in_bytes'),
                                                   out_bytes=interface.get('out_bytes'))
                router_info_list.append(interface_info)
        except Exception as e:
            print(e)
            pass

    # 写入数据库并提交
    session.add_all(router_info_list)
    session.commit()


if __name__ == '__main__':
    get_info_writedb(ip_list, 'qytangro')
