li = list(map(int,input().split()))
di = {}
for i in li:
    if i in di:
        di[i] = di[i] + 1
    else:
        di[i] = 1
for digit,count in di.items():
    print(f"{digit} Occures {count} time(s)")

'''
1 2 2 3 3 3 4 4 4 4
1 Occures 1 time(s)
2 Occures 2 time(s)
3 Occures 3 time(s)
4 Occures 4 time(s)
'''