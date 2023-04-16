import pickle

dbfile=open('people_pickle.pl', 'rb')
db=pickle.load(dbfile)
for i in db:
    print(i, '=>',db[i])