#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
import datetime
import os

tzutc_8 = datetime.timezone(datetime.timedelta(hours=8))  # 设置时区为东八区

# os.path.dirname(os.path.realpath(__file__) 当前文件目录
db_file_name = f'{os.path.dirname(os.path.realpath(__file__))}{os.sep}sqlalchemy_syslog_sqlite3.db'

engine = create_engine(f'sqlite:///{db_file_name}?check_same_thread=False',
                       # echo=True
                       )

Base = declarative_base()


class DeviceConfig(Base):
    __tablename__ = 'device_config'

    id = Column(Integer, primary_key=True)
    device_ip = Column(String(64), nullable=False, index=True)
    device_config = Column(String(99999), nullable=False)
    config_md5 = Column(String(100), nullable=False)
    record_time = Column(DateTime(timezone='Asia/Chongqing'), default=datetime.datetime.now)

    def __repr__(self):
        return f"{self.__class__.__name__}(Device IP: {self.device_ip} " \
               f"| Datetime: {self.record_time} " \
               f"| Config MD5: {self.config_md5})"


if __name__ == '__main__':
    # 如果希望删除老的数据就取消注释
    if os.path.exists(db_file_name):
        os.remove(db_file_name)
    # checkfirst=True，表示创建表前先检查该表是否存在，如同名表已存在则不再创建。其实默认就是True
    Base.metadata.create_all(engine, checkfirst=True)
