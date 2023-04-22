import sys
sys.path.extend(['/root/Python_Github_Code'])

from sqlite_router_cpu_mem import RouterMonitor,engine
from snmpv2_getall import snmpv2_getall
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

ip_list=['10.1.1.1','10.1.1.2']

def get_info_writedb(ip_list, rocommunity):
    router_info_list=[]
    for ip in ip_list:
        try:
            get_all=snmpv2_getall(ip,rocommunity)

            router_info=RouterMonitor(device_ip=get_all.get('ip'),
                                      cpu_useage_percent=get_all.get('cpu_usage'),
                                      mem_use=get_all.get('mem.usage'),
                                      mem_free=get_all.get('mem_free')
                                      )
            router_info_list.append(router_info)
        except Exception:
            pass

    session.add_all(router_info_list)
    session.commit()

if __name__ == '__main__':
    get_info_writedb(ip_list,'kevinro')

