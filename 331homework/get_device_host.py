from ssh_moudule import q_ssh
import re
import hashlib
import time


# ARM芯片无cisco router 环境
# 第一个函数用于获取设备hostname！
def q_get_config(ip, username, password):
    try:
        full_systemname = q_ssh(ip, username, password, cmd='hostnamectl status')
        split_systemname = re.split('\nTransient\s\S+.\s\w*\n', full_systemname)
        replace_systemname = full_systemname.replace(split_systemname[0], '')
        split_systemname_2 = re.split('\n\s*Architecture.\s\w*\n', full_systemname)
        # print(split_systemname_2)
        replace_systemname_2 = replace_systemname.replace(split_systemname_2[1], '')
        return replace_systemname_2

    except Exception:
        return


def q_check_diff(ip, username, password):
    begin_md5 = ''
    while True:
        linux_hostname = q_get_config(ip, username, password)
        m = hashlib.md5()
        m.update(linux_hostname.encode())
        md5_result = m.hexdigest()
        print(md5_result)
        if not begin_md5:
            begin_md5 = md5_result
        elif begin_md5 != md5_result:
            print('MD5 value changed')
            break
        time.sleep(5)


if __name__ == '__main__':
    # print(q_get_config('192.168.139.128', username='kevin', password='sy30323604.'))
    print(q_check_diff('192.168.139.128', username='kevin', password='sy30323604.'))
