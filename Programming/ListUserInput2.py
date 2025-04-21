li = input("Enter space separated element: ")
li = li.split()
print(li)

'''
Enter space separated element: 13 43 65 76 77
['13', '43', '65', '76', '77']
'''

li = list(map(int,li))
print(li)

tup = tuple(map(int,input("Enter space separated Element ").split()))
print(tup)
'''
Enter space separated Element 12 34 55 33 21
(12, 34, 55, 33, 21)
'''

li2 = list(map(int,input().split()))
print([i for i in li2 if i % 2 == 0 ])
'''
12 23 44 66 87 55 22
[12, 44, 66, 22]
'''