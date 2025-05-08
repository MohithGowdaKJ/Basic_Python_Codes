# if str has integer value then conversion is allowed
a = 30
print(a,type(a))
b = int(a)
print(b,type(b))

#str to integer conversion is not allowed in python 
x = 'Kod'
print(x,type(x))
y = int(x) 
# print(y,type(y)) # Error

p = float(input("Enter float type data"))
print(p,type(p))

#While converting int to bool for all non zero value we will get true
#While converting int to bool for 0 and empty string we will get false    
q = 12
print(q,type(q))
q = bool(q)
print(q,type(q)) #True
m = 'jfj'
print(m,type(m))
m = bool(m)
print(m,type(m)) #True
n = ''
print(n,type(n))
n = bool(n)
print(n,type(n)) # False

