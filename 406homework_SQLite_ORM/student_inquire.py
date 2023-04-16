from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime
import datetime
from sqlalchemy.orm import sessionmaker, declarative_base

# ------------------sqlite3--------------------------------
engine = create_engine('sqlite:///sqlalchemy_sqlite3.db?check_same_thread=False',  # echo=True
                       )

Base = declarative_base()

Session = sessionmaker(bind=engine)

# 创建session对象

session = Session()


class UserHomeWork(Base):
    __tablename__ = 'user_homework'
    id = Column(Integer, primary_key=True)
    student_name = Column(String(64), nullable=False, index=True)
    age = Column(Integer, nullable=False)
    homework_account = Column(Integer, nullable=False)
    last_update_time = Column(DateTime(timezone='Asia/Chongqing'), default=datetime.datetime.now)

    def __repr__(self):
        return f"{self.__class__.__name__}(学院姓名：{self.student_name} | 学院年龄: {self.age} | " \
               f"作业数量：{self.homework_account} | 最后更新时间：{self.last_update_time})"


if __name__ == '__main__':
    # 创建数据库
    Base.metadata.create_all(engine, checkfirst=True)

    # 第一次创建表时，插入下方数据
    homework_dict = [
        {'student_name': '张三', 'age': 37, 'homework_account': 1},
        {'student_name': '李四', 'age': 33, 'homework_account': 5},
        {'student_name': '王五', 'age': 32, 'homework_account': 10},
    ]

    # 添加数据
    for homework in homework_dict:
        homework_obj = UserHomeWork(**homework)
        session.add(homework_obj)

    # 提交
    session.commit()


