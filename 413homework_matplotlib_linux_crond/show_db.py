from sqlite_router_cpu_mem import RouterMonitor, engine
from write_db import ip_list
from sqlalchemy.orm import sessionmaker
from random import choice
from pprint import pprint
from datetime import datetime, timedelta
from matplotlib_line_graph import mat_line

Session = sessionmaker(bind=engine)
session = Session()

now = datetime.now()
one_hours_before = now - timedelta(hours=1)

color_list = ['red', 'blue', 'green', 'yellow']

line_style_list = ["solid", "dashed"]

cpu_line_list = []

mem_line_list = []

i = 0

for ip in ip_list:

    router_infos = session.query(RouterMonitor).filter(RouterMonitor.record_datetime >= one_hours_before,
                                                       RouterMonitor.device_ip == ip
                                                       )
    time_list = []
    cpu_list = []
    mem_list = []

    for router_info in router_infos:
        time_list.append(router_info.record_datetime)
        cpu_list.append(router_info.cpu_useage_percent)

        mem_use = router_info.mem_use
        mem_free = router_info.mem_free
        mem_percent = round((mem_use / (mem_use + mem_free)) * 100, 2)

        mem_list.append(mem_percent)

    cpu_line_list.append([time_list, cpu_list, choice(line_style_list), color_list[i], ip])

    mem_line_list.append([time_list, mem_list, choice(line_style_list), color_list[i], ip])

    i += 1



mat_line(cpu_line_list, 'CPU利用率', '百分比')
mat_line(mem_line_list, 'MEM利用率', '百分比')
