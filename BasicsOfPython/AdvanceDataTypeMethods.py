# List will always accept Iterable object
li1 = list('Mohith')
print(li1) #['M', 'o', 'h', 'i', 't', 'h']

li2 = list((10,'hi',20.3))
print(li2) #[10, 'hi', 20.3]

li3 = list({'mohith',20.22,22})
print(li3) #['mohith', 20.22, 22]

li4 = list({'name':'Mohith','age':22})
print(li4) #['name', 'age']

li5 =list(range(1,11))
print(li5) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tuple will always accept Iterable Object
tup1 = tuple({10, 20, 30, 40})
print(tup1)

tup2 = tuple("Mohith")
print(tup2)

tup3 = tuple([10,20,30,40])
print(tup3)

tup4 = tuple({'name':'Mohith','age':22})
print(tup4)

tup5 = tuple(range(1,11))
print(tup5)

# Tuple will always accept Iterable Object
set1 = set((10, 20, 30, 40))
print(set1)

set2 = set("Mohith")
print(set2)

set3 = set([10,20,30,40])
print(set3)

set4 = set({'name':'Mohith','age':22})
print(set4)

set5 = set(range(1,11))
print(set5)

# Dict will always accept Iterable objects but in key value pairs
dict1 = dict([['name','Mohith'],['age',22]])
print(dict1)