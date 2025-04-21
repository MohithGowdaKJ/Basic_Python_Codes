print(bool('')) #false
print(bool(0)) #false
print(bool("fghj")) #true
print(bool(32)) #True
print(int('hhjj')) #Error
print(int('23')) #23
print(int('23.33')) #Error
print(int(23.33)) #23
print(float('23.33')) #23.33

#Taking Float value from user and converting into integer value
value = int(float(input("Enter Price: Float value ")))
print(value,type(value))