import datetime

now = datetime.datetime.now()

hours120 = now - datetime.timedelta(hours=120)

hours120.strftime("%Y-%m-%d_%H-%M-%S")

filename = 'save_fivedayago_time_' + hours120.strftime("%Y-%m-%d_%H-%M-%S") + 'txt'
#打开一个文件，文件名是变量filename的字符串内容，a代表如已有文件，将内容添加进文件
with open(filename, 'a') as file_object:
    file_object.write('405')
