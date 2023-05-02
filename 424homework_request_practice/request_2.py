#!/usr/bin/env python3
# -*- coding=utf-8 -*-


import requests
from requests.auth import HTTPBasicAuth


# HTTP Basic认证
r = requests.get('http://10.1.1.1/level/15/exec/-/show/ip/interface/brief/CR',
                 auth=HTTPBasicAuth('admin', 'admin'))

print(r.text)

