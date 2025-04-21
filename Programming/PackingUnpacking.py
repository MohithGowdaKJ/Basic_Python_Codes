a, b, c = 10, 20, 30
print(a)
print(b)
print(c)
name,age = 'Mohith',23
print(name)
print(age)
name,age,*marks = 'Mohith',23,88,99,87,92
print(name)
print(age)
print(marks)
'''
Mohith
23
[88, 99, 87, 92]
'''
name,*marks,age = 'Mohith',99,87,78,92,23
print(name)
print(marks)
print(age)
'''
Mohith
[99, 87, 78, 92]
23
'''