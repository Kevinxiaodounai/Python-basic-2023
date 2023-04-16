from initdata import db
from datetime import date
import pickle

dbfile=open('people_pickle.pl', 'wb')
pickle.dump(db,dbfile)
dbfile.close()
#
# dbfile=open('people_pickle.pl','wb')
# pickle.dump({'today':date.today()},dbfile)
# dbfile.close()
