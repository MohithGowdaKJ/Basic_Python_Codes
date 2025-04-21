'''
1. In tuple we can store Homo and Hetero type of data
2. In tuple we can store duplicate values
3. Tuples are ordered collection of data.
4. Tuples are Immutable: Once we declare the tupple we can not modify it
'''

tup = (1,2.3,'Mohith',True)
# tup.pop() #Error
# tup.remove(1) #Error
# tup.append(23) #Error

del tup #Delete the entire tuple

tup1 = (1, 2, 3, 4)
tup2 = (5, 6, 7, 8)
tup3 = tup1 + tup2
print(tup3) #It will concatinate two tuples

tup4 = (10,) #Singleton tuple => a tupple with only one ele and coma will indicate singleton tupple
print(tup4,type(tup4))

#Unpacking of tupple
tup5 = (1,2,3,4,5)
#ele1 = tup5[1]
#ele2 = tup5[2]
ele1,ele2,ele3,ele4,ele5 = tup5
print(f"The value of ele1: {ele1}")
print(f"The value of ele2: {ele2}")
print(f"The value of ele3: {ele3}")
print(f"The value of ele4: {ele4}")
print(f"The value of ele5: {ele5}")