list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

for a in list1:
    if a not in list2:
        print(str(a)+' only in List1')
    else:
        print(str(a)+' in list1 and list2')

