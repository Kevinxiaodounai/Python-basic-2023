import shelve

db = shelve.open('people_shelve')
for i in db:
    print(i, '=>', db[i])
db.close()
