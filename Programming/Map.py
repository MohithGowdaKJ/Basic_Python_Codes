def double(x):
    return x*2

li = [21, 34, 55, 25]
double_li = list(map(double,li))
print(double_li)

tup = ['22', '37', '21', '77']
print(tup)
tup = tuple(map(int,tup))
print(tup)

li3 = [11, 23, 44]
print(li3)
li3 = list(map(float,li3))
print(li3)