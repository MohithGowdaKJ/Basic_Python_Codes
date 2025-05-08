li = list(map(int,input().split()))
di = {}
for i in li:
    if i in di:
        di[i] = di[i] + 1
    else:
        di[i] = 1
print(di)
for digit,count in di.items():
    print(f"{digit} Occures {count} time(s)")

'''
1 2 3 2 4 6 1 3 5 2 1 
{1: 3, 2: 3, 3: 2, 4: 1, 6: 1, 5: 1}
1 Occures 3 time(s)
2 Occures 3 time(s)
3 Occures 2 time(s)
4 Occures 1 time(s)
6 Occures 1 time(s)
5 Occures 1 time(s)
'''