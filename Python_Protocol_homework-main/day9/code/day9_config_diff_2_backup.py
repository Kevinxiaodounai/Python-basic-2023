#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import re
import hashlib
from new_homework.day7.code.day7_1_create_db import Router, DeviceConfig, engine
from sqlalchemy.orm import sessionmaker
# 导入正课中的netmiko代码
from new_homework.day7.code.tools.ssh_client_netmiko import netmiko_show_cred

# 协程相关
import asyncio
import os
import threading

Session = sessionmaker(bind=engine)
session = Session()

# 协程任务循环
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


# 定义netmiko的携程函数
async def async_netmiko_show(task_id, ip, username, password, cmd):
    print(f'ID: {task_id} Started')
    print(os.getpid(), threading.currentThread().ident)
    result = await loop.run_in_executor(None, netmiko_show_cred, ip, username, password, cmd)
    print(f'ID: {task_id} Stopped')
    return result


# 循环任务计数号
task_no = 1

# 协程的任务清单
tasks = []

for router in session.query(Router).all():
    # 产生携程任务
    task = loop.create_task(async_netmiko_show(task_no,
                                               router.ip,
                                               router.username,
                                               router.password,
                                               "show run"))
    # 把产生的携程任务放入任务列表
    tasks.append(task)
    # 任务号加1
    task_no += 1

loop.run_until_complete(asyncio.wait(tasks))

result_list = []
for i in tasks:
    result_list.append(i.result())

for device_config_raw, ip in result_list:
    split_result = re.split(r'\nhostname \S+\n', device_config_raw)
    device_config = device_config_raw.replace(split_result[0], '').strip()
    m = hashlib.md5()
    m.update(device_config.encode())
    md5_value = m.hexdigest()
    device_obj = session.query(Router).filter_by(ip=ip).one()
    device_db_obj = DeviceConfig(router=device_obj,
                                 device_config=device_config,
                                 config_md5=md5_value)
    session.add(device_db_obj)
    session.commit()


for device_config in session.query(DeviceConfig):
    print(device_config)