#!/usr/bin/env python3
# -*- coding=utf-8 -*-


from sqlalchemy.orm import sessionmaker
from new_homework.day8.code.day8_syslog_1_create_db import Syslog, engine
from sqlalchemy import func
from new_homework.day3.code.tools.day3_bing import mat_bing
import os

Session = sessionmaker(bind=engine)
session = Session()

# 严重级别名字列表
severity_level_name_list = []
# 严重级别数量列表
severity_level_count_list = []

# 数据库中找到严重级别名字, 严重级别数量的信息, 并写入列表
for level, count in session.query(Syslog.severity_level_name, func.count(Syslog.severity_level_name)).group_by(
        Syslog.severity_level_name).all():
    severity_level_name_list.append(level)
    severity_level_count_list.append(count)

# print(severity_level_name_list)
# print(severity_level_count_list)

# 发送SYSLOG设备的IP列表
device_ip_list = []
# 设备发送SYSLOG数量列表
device_log_count_list = []

# 数据库中找到发送SYSLOG设备的IP, 设备发送SYSLOG数量的信息, 并写入列表
for ip, count in session.query(Syslog.device_ip, func.count(Syslog.device_ip)).group_by(
        Syslog.device_ip).all():
    device_ip_list.append(ip)
    device_log_count_list.append(count)

# print(device_ip_list)
# print(device_log_count_list)

# 文件保存路径
current_dir = os.path.dirname(os.path.realpath(__file__))
save_file_severity_level = f'{current_dir}{os.sep}severity_level.png'
save_file_device_ip = f'{current_dir}{os.sep}device_ip.png'

# 使用饼状图呈现
mat_bing(severity_level_name_list, severity_level_count_list, 'SYSLOG严重级别分布图', save_file_severity_level)
mat_bing(device_ip_list, device_log_count_list, 'SYSLOG设备分布图', save_file_device_ip)