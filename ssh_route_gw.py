import paramiko
import re

def q_ssh(ip, username, password, port=22, cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x


def ssh_get_route(ip, username, password, port=22, cmd='netstat -rn'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    a = re.findall('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\s*UGScg', x)[0]
    b = a[0:12]
    return b


if __name__ == '__main__':
    print(q_ssh('127.0.0.1', 'xiaodounai', 'sy30323604.'))
    print(q_ssh('127.0.0.1', 'xiaodounai', 'sy30323604.', cmd='pwd'))
    print('网关为：')
    print(ssh_get_route('127.0.0.1', 'xiaodounai', 'sy30323604.'))
