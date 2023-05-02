#!/usr/bin/env python3
# -*- coding=utf-8 -*-


import os
import os.path
import base64

from system_cmd import system_cmd
from flask import Flask, request
import json

node = Flask(__name__)
node.debug = True
server_file_dir=f'{os.path.dirname(os.path.realpath(__file__))}{os.sep}server_file_dir{os.sep}'

# POST实现JSON RPC
@node.route('/cmd', methods=['POST'])
def cmd():
    client_post_data = request.json
    # 如果存在JSON数据
    if client_post_data:
        # 提取键'cmd',如果JSON格式错误，返回‘json foramt error'的报错
        try:
            cmd_command = client_post_data.get('cmd')
        except AttributeError:
            return {'error': base64.b64encode('json format error'.encode()).decode()}

        if cmd_command:
            cmd_result = system_cmd(cmd_command)
            # 成功是0号，1号是失败
            if cmd_result[1]:
                return {'error': base64.b64encode(cmd_result[1].encode()).decode()}
            else:
                return {'cmd': cmd_command, 'cmd_result': base64.b64encode(cmd_result[0].encode()).decode()}
        else:
            return {'error': base64.b64encode('json format error'.encode()).decode()}
    else:
        return {'error': base64.b64encode('json format error'.encode()).decode()}


@node.route('/upload', methods=['POST'])
def upload():
    client_post_data = request.json
    if client_post_data:
        try:
            upload_filename = client_post_data.get('upload_filename')
            file_bit = client_post_data.get('file_bit')
        except AttributeError:
            return {'error': base64.b64encode('json format error'.encode()).decode()}
        if upload_filename and file_bit:
            fp = open(server_file_dir + upload_filename, 'wb')
            fp.write(base64.b64decode(file_bit.encode()))
            fp.close()
            return {'message': 'Upload Success', 'upload_filre': upload_filename}
        else:
            return {'error': 'need upload_filename and file_bit'}
    else:
        return {'error': 'no json data'}


@node.route('/download', methods=['POST'])
def download():
    client_post_data = request.json
    if client_post_data:
        try:
            download_filename = client_post_data.get('download_filename')
        except AttributeError:
            return {'error': base64.b64encode('json format error'.encode()).decode()}
        if download_filename:
            if os.path.exists(server_file_dir + download_filename):
                download_json = {'download_filename': download_filename}

                file_bit = base64.b64encode(open(server_file_dir + download_filename, 'rb').read()).decode()

                download_json['file_bit'] = file_bit

                return download_json

            else:
                return {'error': 'download file not exist'}
        else:
            return {'error': 'need download_filename '}
    else:
        return {'error':'no json data'}

if __name__ == "__main__":
    # 运行Flask在host='192.168.1.200', port=8080
    # 在linux上可以使用'0.0.0.0'
    node.run(host='0.0.0.0', port=8080)
