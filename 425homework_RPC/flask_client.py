import requests
import base64
import os
import sys
# -*- coding=utf-8 -*-

server_ip = '172.16.158.129'
server_port = '8080'
base_url = 'http://' + server_ip + ':' + server_port + '/'
exec_cmd_url = base_url + 'cmd'  # 执行命令的URL
upload_url = base_url + 'upload'  # 上传文件URL
download_url = base_url + 'download'  # 下载文件的URL

upload_file_dir=f'{os.path.dirname(os.path.realpath(__file__))}{os.sep}client_upload_file_dir{os.sep}'
download_file_dir=f'{os.path.dirname(os.path.realpath(__file__))}{os.sep}client_download_file_dir{os.sep}'

def json_rpc_client_exec_cmd(obj):
    return_json = requests.post(exec_cmd_url, json=obj).json()
    if return_json.get('cmd_result'):
        return base64.b64decode(return_json.get('cmd_result')).decode('utf-8')
    else:
        return base64.b64decode(return_json.get('error')).decode('utf-8')


def json_rpc_client_upload(filename):
    upload_json = {'upload_filename': filename}

    with open(upload_file_dir + 'logo.jpg', 'rb') as f:
        file_bit = base64.b64encode(f.read()).decode()

    upload_json['file_bit'] = file_bit

    r=requests.post(upload_url,json=upload_json)
    return r.json()

def json_rpc_client_download(filename):
    download_json = {'download_filename': filename}
    return_data = requests.post(download_url,json=download_json).json()
    download_filename=return_data.get('download_filename')

    file_bit = return_data.get('file_bit')

    if download_filename and file_bit:

        with open(download_file_dir+ download_filename,'wb') as f:
            f.write(base64.b64decode(file_bit.encode()))
        print(download_filename+'下载成功')
    else:
        print(return_data.get('error'))




if __name__ == '__main__':
    exec_cmd = {'cmd': 'ifconfig'}
    print(json_rpc_client_exec_cmd(exec_cmd))  # 1

    exec_cmd = {'cmd': 'pwd1'}
    print(json_rpc_client_exec_cmd(exec_cmd))  # 2

    exec_cmd = {'cmd1':'pwd'}
    print(json_rpc_client_exec_cmd(exec_cmd))  # 3

    print(json_rpc_client_upload('logo.jpg'))  # 4

    print(json_rpc_client_download('logo.jpg'))  # 5
    #
    print(json_rpc_client_download('logo1.jpg'))  # 6
