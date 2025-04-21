'''
1. In set we can store Homo as well as Hetero data
2. Set is am Unordered Collection of Data.
3. Set does not support indexing of data.
4. In set we cannot store duplicate values.
5. Set are Mutable
'''

set = {10,20,"Mohith",True,20}
print(set,type(set))
#print(set[1]) #error

#add() => will add ele to the set
set.add(22)
print(set)

#remove() => will remove ele
set.remove(20)
print(set)

#pop() => without index will delete random ele
set.pop()
print(set)
