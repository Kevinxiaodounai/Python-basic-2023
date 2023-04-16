from netmiko import ConnectHandler
import hashlib

# 定义路由器的连接信息
def netmiko_show(ip,username,password,cmd,secret):
    router = {
        'device_type': 'cisco_ios_telnet',
        'ip': ip,
        'username': username,
        'password': password,
        'secret': secret,
        'port': 5003
    }
    try:
    # 连接到路由器
        net_connect = ConnectHandler(**router)
    # 进入特权模式
        net_connect.enable()
    # 获取运行配置文件
        return net_connect.send_command(cmd)
    # # 将配置文件保存到文件中
    # with open('running-config.txt', 'w') as f:
    #     f.write(output)

    # # 关闭连接
    # net_connect.disconnect()

    except Exception as e:
        print(f'connection error ip: {ip} error: {str(e)}')


def compute_hash(s, algorithm='sha256'):
    hash_object = hashlib.new(algorithm)
    hash_object.update(s.encode('utf-8'))
    return hash_object.hexdigest()

def get_show_run(ip, username, password):
    show_run_raw=netmiko_show(ip,username,password,'show run','cisco')
    show_run= 'hostname' + show_run_raw.split('\nhostname ')[1]

    return show_run.strip(), compute_hash(show_run.strip())

if __name__=='__main__':

    print(get_show_run('127.0.0.1','cisco','cisco123'))
