from initdata import cq_bomb , tina
import shelve
from datetime import datetime

db=shelve.open('people_shelve')
db['cq_bomb']=cq_bomb
db['tina']=tina
db['dateime']=datetime.now()
db.close()