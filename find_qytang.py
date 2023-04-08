import os

print('文件中包含"qytang"关键字的文件为：')
os.chdir('test')

for file_or_dir in os.listdir(os.getcwd()):
    if os.path.isfile(file_or_dir) is True:
        with open(file_or_dir) as file_object:
            content=file_object.read()
            if 'qytang' in content:
                print(file_or_dir)
#     # else:
#     #     # os.chdir(file_or_dir)
#
#         # # files=(open(file_or_dir),f"*{keyword}*")
#         # # print(files)
#         # print(file_or_dir)