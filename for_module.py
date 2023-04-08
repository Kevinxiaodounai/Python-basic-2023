list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

def f(x,y):
    for a in x:
        if a not in y:
            print(str(a) + ' only in List1')
        else:
            print(str(a) + ' in list1 and list2')

f(list1,list2)