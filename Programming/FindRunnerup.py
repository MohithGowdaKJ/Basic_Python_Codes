li = list(map(int,input().split()))
li1 = list(set(li))
li1.sort(reverse=True)
print('The second Largest Number is:',li1[1])
print('The Largest Number is:',li1[0])
print('The Smallest Number is:',li1[-1])

'''
77 22 11 4 89 11 54 22 67 
The second Largest Number is: 77
The Largest Number is: 89
The Smallest Number is: 4
'''