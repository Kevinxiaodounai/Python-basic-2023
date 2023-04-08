import paramiko


def q_ssh(ip, username, password, port=22, cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x


if __name__ == '__main__':
    # print(q_ssh('127.0.0.1', 'xiaodounai', 'sy30323604.'))
    print(q_ssh('172.16.158.129', 'kevin', 'sy30323604.', cmd='pwd'))
