from student_inquire import UserHomeWork, session

# 查询所有数据库
# student = session.query(UserHomeWork).all()
# for i in student:
#     print(i)

# 查询用户名
# input()
# student = session.query(UserHomeWork).filter_by(student_name='张三').one()
# print(student)

# 查询
user_notify = """
请输入查询选项：
输入 1:查询整个数据库
输入 2:根据学员姓名查询
输入 3:根据学院年龄查询
输入 4:根据作业数量查询
输入 0：退出
"""

while True:
    print(user_notify)
    user_input = input('请输入查询选项： ')
    if user_input == '0':
        break
    elif user_input == '1':
        homework = session.query(UserHomeWork).all()
        for homework in homework:
            all_homework = f'学院姓名：{homework.student_name} | 学院年龄 ： {homework.age} | '\
                           f'作业数量：{homework.homework_account} | 最后更新时间： {homework.last_update_time}'
            print(all_homework)
    elif user_input =='2':
        user_name=input('请输入学院姓名： ')
        if not user_name:
            continue
        homework=session.query(UserHomeWork).filter_by(student_name=user_name).first()
        if not homework:
            print('学员信息未找到！')
        else:
            all_homework = f'学院姓名：{homework.student_name} | 学院年龄 ： {homework.age} | ' \
                           f'作业数量：{homework.homework_account} | 最后更新时间： {homework.last_update_time}'
            print(all_homework)
    elif user_input =='3':
        user_age=input('搜索大于输入年龄的学员，请输入学员年龄： ')
        if not user_age:
            continue
        homework=session.query(UserHomeWork).filter(UserHomeWork.age > user_age).all()
        if not homework:
            print('学员信息未找到！')
        else:
            for homework in homework:
                all_homework = f'学院姓名：{homework.student_name} | 学院年龄 ： {homework.age} | ' \
                           f'作业数量：{homework.homework_account} | 最后更新时间： {homework.last_update_time}'
                print(all_homework)
    elif user_input =='4':
        user_homework=input('搜索大于输入作业数的学员，请输入作业数量： ')
        if not user_homework:
            continue
        homework=session.query(UserHomeWork).filter(UserHomeWork.homework_account > user_homework).all()
        if not homework:
            print('学员信息未找到！')
        else:
            for homework in homework:
                all_homework = f'学院姓名：{homework.student_name} | 学院年龄 ： {homework.age} | ' \
                           f'作业数量：{homework.homework_account} | 最后更新时间： {homework.last_update_time}'
                print(all_homework)
    else:
        print('输入有误，请重新输入！')
