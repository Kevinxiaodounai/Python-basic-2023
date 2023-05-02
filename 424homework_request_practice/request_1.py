import os.path

import requests

# 自定义头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/112.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
              'q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'}
r = requests.get('https://qytsystem.qytang.com/static/images/logo.jpg', headers=headers)

imgContent = r.content

imgefile = open('../425homework_RPC/client_upload_file_dir/logo.jpg', 'wb')
imgefile.write(imgContent)
imgefile.close()


# def parse_http_header(filename):
#     header_dict = {}
#     for line in open(filename.'r'):
#         line_split = line.strip().split(':')
#         header_dict[line_split[0].strip()] = line_split[1].strip()
#     return header_dict
#
# download_file_dir=f'{os.path.dirname(os.path.realpath(__file__))}{os.sep}download_file{os.sep}'