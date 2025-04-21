"""
1. in list we can store Homogeneous and Heterogeneous data.
2. In list we can store Dupicate Values.
3. List is an ordered collection of data: Order of 
   insertion will be remain as it is in the output.
4. Lists are Mutable: Once declare the can be Modified.
"""
li = [1,22,"Mohith",'A',True,22]
print(li,type(li))
print(li[2])

# append(): Will add element at the end of the list
li.append(300)

# insert(index,element): insert an ele at specified index
li.insert(1,20)
print(li)

#remove(ele): Removes the first Occurrence of list
li.remove(22)
print(li)

# in and not in Operator:
print(2000 in li) #False
print("Mohith" in li) #True

#pop(): without argument will delete and return the last ele
remove_ele = li.pop()
print(li)
print(remove_ele)

#pop(index): With argument ill delete the ele at specified index.
remove = li.pop(2)
print(remove)

#del keyword => it will delete the last ele but it wont return 
del li[1]
print(li)

del li # it will delete the complete lists