#Without input and without return type
def add():
    a = 10
    b = 20
    print("Addition of a and b is: ",a+b)

#With Parameter and without return type
def sub(a,b):
    print(a-b)

#Without parameter and with return type
def mul():
    return 10*20

#With parameter and return type
def div(a,b):
    return a/b 

add()
sub(10,20)
print(mul())   
print(div(10,5))   
