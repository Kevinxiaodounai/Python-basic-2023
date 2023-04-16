import paramiko
import argparse

# 创建参数解析器
parser = argparse.ArgumentParser(description='SSH登录脚本')

# 添加参数
parser.add_argument('-i', '--ip', type=str, required=True, help='IP地址')
parser.add_argument('-u', '--username', type=str, required=True, help='用户名')
parser.add_argument('-p', '--password', type=str, required=True, help='密码')
parser.add_argument('-c', '--command', type=str, required=True, help='命令')

# 解析参数
args = parser.parse_args()

# 创建SSH客户端
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接SSH服务器
client.connect(args.ip, username=args.username, password=args.password)

# 执行命令
stdin, stdout, stderr = client.exec_command(args.command)

# 输出结果
print(stdout.read().decode())

# 关闭连接
client.close()
