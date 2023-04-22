from netmiko import ConnectHandler
import re
from import_matplotlib import mat_bing
device = {
    'device_type': 'cisco_ios',
    'ip': '10.1.1.1',
    'username': 'admin',
    'password': 'cisco123',
    'secret': 'cisco123',
}

with ConnectHandler(**device) as net_connect:
    output = net_connect.send_command('show flow monitor name qytang-monitor cache format table')
    get_name_list = []
    get_count_list = []
    # print(output)
    for line in output.strip().split('\n'):
        app_name = re.match('((port|layer7)\s\w*)\s*(\d*)', line)
        if app_name:
            get_name_list.append(app_name.groups()[0])
            get_count_list.append(app_name.groups()[2])
    # print(get_name_list)
    # print(get_count_list)
    mat_bing(get_name_list,get_count_list,'Netflow')