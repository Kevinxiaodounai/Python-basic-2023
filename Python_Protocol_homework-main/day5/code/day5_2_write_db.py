#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# 在Linux使用crond调度运行, 需要添加项目主目录到搜索路径
import sys
sys.path.extend(['/python_homework_protocol/'])

# pip3 install influxdb
from new_homework.day4.code.tools.day4_snmp_get_all import snmpv2_getall
import datetime
from influxdb import InfluxDBClient

# 设备IP地址列表
ip_list = ['10.1.1.1', '10.1.1.2']

# SNMP RO Community
snmp_community = "qytangro"

# influx DB 主机IP地址
influxdb_host_ip = "10.1.1.11"

# 连接influxDB 数据库
client = InfluxDBClient(influxdb_host_ip, 8086, 'qytdbuser', 'Cisc0123', 'qytdb')

# 本次采集的所有路由器记录的列表
record_list = []

# 逐个路由器采集CPU和内存数据
for router_ip in ip_list:
    # 获取特定路由器的全部SNMP信息
    getall_result = snmpv2_getall(router_ip, snmp_community)

    # 格式化当前时间
    current_time = datetime.datetime.utcnow().isoformat("T")

    # measurement 略等于 表
    # time   : 记录时间
    # tags   : 用于后续过滤
    # fields : 记录详细内容
    cpu_mem_body = {
                    "measurement": "router_monitor",
                    "time": current_time,
                    "tags": {
                        "device_ip": getall_result.get('ip'),
                        "device_type": "IOS-XE"
                        },
                    "fields": {
                        "cpu_usage": getall_result.get('cpu_usage'),
                        "mem_usage": getall_result.get('mem_usage'),
                        "mem_free": getall_result.get('mem_free'),
                        },
                    }
    # 写入列表, 便于统一写入数据库
    record_list.append(cpu_mem_body)

# 一次性把多个设备采集的内容写入数据库
client.write_points(record_list)

