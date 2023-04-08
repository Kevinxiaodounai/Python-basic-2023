from ping_moudule import qping
from ssh_moudule import q_ssh
import re
import pprint


def q_get_if(*ips, username='', password=''):
    device_if_dict = {}
    for ip in ips:
        if_dict = {}
        if qping(ip):
            # 目标 将可以ping通的IP，SSH登陆后，执行'route -n' 将 Destination Gateway Genmask 3个字段的值存储为if_dict字典的IP键值
            for line in q_ssh(ip, username, password, cmd='route -n').split('\n'):
                print(line)
                re_result = re.match(
                    '(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s*(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s*(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s*\w*\s*\d*\s*\d\s*\d\s(\w*\d*)',
                    line.strip())
                print(re_result)
                if re_result:
                    if_dict[re_result.groups()[3]] = re_result.groups()[0]
        device_if_dict[ip] = if_dict  # 键 的值是 if_dict这个字典
    return device_if_dict


if __name__ == '__main__':
    pprint.pprint(q_get_if('10.10.10.10', '172.16.158.129', username='kevin', password='sy30323604.'), indent=4)
