import re
str1='Port-channel1.89      192.168.189.254   YES CONFIG   up'
a=re.match('([A-Z]\S+\d)\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+YES CONFIG\s+([a-z][a-z])',str1).groups()
int='接口地址'
ipadd='IP地址'
stat='状态'

line1=("%-14s:" % int)+a[0]
line2=("%-15s:" % ipadd)+a[1]
line3=("%-15s:" % stat)+a[2]
print(line1)
print(line2)
print(line3)