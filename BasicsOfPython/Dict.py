# dict is mutable
dict = {'name':'Mohith','Age': 22, 'Phone': 1234567,'Age': 27} #{'name': 'Mohith', 'Age': 27, 'Phone': 1234567} <class 'dict'>
print(dict,type(dict))

# In dict we cannot store duplicate keys 
dict['name'] = 'Rohith'
print(dict)

# In dict we can store duplicate values
marks = {'Science':85, 'Maths': 85}


for i in dict.keys():
   print(i)

for i in dict.values():
   print(i)

for i in dict.items():
   print(i)
