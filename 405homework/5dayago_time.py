import datetime

now = datetime.datetime.now()

hours120 = now - datetime.timedelta(hours=120)

hours120.strftime("%Y-%m-%d_%H-%M-%S")

filename = 'save_fivedayago_time_' + hours120.strftime("%Y-%m-%d_%H-%M-%S") + 'txt'

with open(filename, 'a') as file_object:
    file_object.write('405')
