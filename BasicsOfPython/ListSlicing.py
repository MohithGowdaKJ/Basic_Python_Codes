# list_name[startIndex:endindex:steps]
li1 = [10,20,30,40,50]
slic1 = li1[1:4:1]
print(slic1) #[20, 30, 40]

slic2 = li1[2:4:]
print(slic2) #[30, 40]

slic3 = li1[::]
print(slic3) #[10, 20, 30, 40, 50]

slic4 = li1[1:4:2]
print(slic4) #[20, 40]

reverse = li1[::-1]
print(reverse) #[50, 40, 30, 20, 10]

last = li1[-1::]
print(last) #[50]

'''
1. Slicing is used to create sublist from main list
2. for reverse syntax => list_name[::-1]
3. for last ele syntax => list_name[-1::]
'''