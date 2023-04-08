#无router环境
import paramiko
import time


def q_multicmd(ip, username, password, cmd_list, enable='', wait_time=2, verbose=True):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)
    chan = ssh.invoke_shell()
    time.sleep(1)
    x = chan.recv(2048).decode()
    if enable and '>' in x:
        chan.send('config ter'.encode())
        chan.send(b'\n')
        time.sleep(wait_time)
        chan.send(enable.encode())
        chan.send(b'\n')
        time.sleep(wait_time)
    elif not enable and '>' in x:
        print('need enable password')
        return
    for cmd in cmd_list:
        chan.send(cmd.encode())
        chan.send(b'\n')
        time.sleep(wait_time)
        x = chan.recv(40960).decode()
        if verbose:
            print(x)
    chan.close()
    ssh.close()


if __name__ == '__main__':
    q_multicmd('192.168.1.1', 'admin', 'cisco123',
               ['terminal length 0', 'show version', 'router ospf 1', 'network 10.0.0.0 0.0.0.255'], enable='cisco123',
               wait_time=2, verbose=True)

