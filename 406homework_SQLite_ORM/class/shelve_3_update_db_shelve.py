import shelve
from datetime import timedelta

from initdata import cq_bomb , tina
import shelve
from datetime import datetime

db=shelve.open('people_shelve')
db['cq_bomb']=cq_bomb
db['tina']=tina
db['dateime']=datetime.now()
db.close()


db = shelve.open('people_shelve')
cq_bomb = db['cq_bomb']  # 读取数据库键‘cq_bomb’中的字典
cq_bomb['salary'] *= 1.6  # 更新字典
db['cq_bomb'] = cq_bomb
db.close()

db = shelve.open('people_shelve')
datetime_now = db['datetime']  # 读取数据库键‘datetime’中的时间对象
datetime_now += timedelta(days=4)  # 在原来的时间基础上+4天
db['datetime'] = datetime_now  # 把更新后的字典重新写回数据库键
db.close()

db = shelve.open('people_shelve')
print(db['cq_bomb'])
print(db['datetime'])
db.close()



