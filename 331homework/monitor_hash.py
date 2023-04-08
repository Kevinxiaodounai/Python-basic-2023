import hashlib

m = hashlib.md5()
# 使用md5
m.update(''.encode())
# test 加密
print(m.hexdigest())
# 输出加密字符串

m.update('test1'.encode())
print(m.hexdigest())
