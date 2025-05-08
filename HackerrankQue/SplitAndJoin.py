li = input().split()
print(li)
s = '-'.join(li)
print(s)

# li2 = [10,20,30,40] Error
li2 = ['10','20','30','40'] #Integer should be in a string format to use join
li2 = ','.join(li2)
print(li2)

'''
This is a sample input
['This', 'is', 'a', 'sample', 'input']
This-is-a-sample-input
10,20,30,40
'''