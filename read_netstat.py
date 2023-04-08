import os
import re
import time

while True:
    try:
        time.sleep(1)
        a = os.popen('lsof -iTCP -sTCP:LISTEN')
        b = a.read()
        c = re.findall(r'TCP\s\S:http', b)
        # print(c)
        print('等待一秒重新开始监控')
        if 'http' in str(c) and 'TCP' in str(c):
            print('HTTP(TCP/80)服务已经被打开')
            break
    except KeyboardInterrupt:
        break
