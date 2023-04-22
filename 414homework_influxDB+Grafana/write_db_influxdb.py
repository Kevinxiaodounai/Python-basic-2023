import sys
sys.path.extend(['/root/Python_Github_Code'])

from snmpv2_getall import snmpv2_getall
import datetime
from influxdb import InfluxDBClient

ip_list = ['10.1.1.1', '10.1.1.2']

snmp_community = 'qytangro'

influxdb_host_ip = '172.16.158.129'

client= InfluxDBClient(influxdb_host_ip, 8086,'qydbuser','Cisc0123','qydb')

record_list = []

for router_ip in ip_list:
    getall_result = snmpv2_getall(router_ip, snmp_community)

    current_time=datetime.datetime.utcnow().isoformat('T')

    cpu_mem_body={
                  'measurement':'router_monitor',
                  'time':current_time,
                  'tags':{
                      'device_ip':getall_result_.get('ip'),
                      'device_type':'IOS-XE'
                    },
                  'fields':{
                      'cpu_usage':getall_result.get('cpu_usage'),
                      'mem_usage':getall_result.get('mem_usage'),
                      'mem_free':getall_result.get('mem_free'),
                    },
                  }
    record_list.append(cpu_mem_body)

client.write_points(record_list)
