# Strings are immutable that means if the variables are declared 
# after that if we try to modify it, the new object will be created
# once Strings are declared we cannot modify it, we need to create a new String to alter it. 
s1 = 'Mohith'
s1.upper()
print(s1) # "Mohith"

s2 = 'Rohith'
s2 = s2.upper()
print(s2) # "ROHITH"

print(id(s2))  # Prints the address of reference variable

s3 = 'Hello'
s4 = 'World'
print(id(s3[0]))
print(id(s3[3]))
print(id(s3[-1]))

print(id(s3[2])) # addresses of all this will be same because of string Interning
print(id(s3[3]))
print(id(s4[3]))

# Python internally usses String Interning
# String interning is a process of checking 
# String intern pool before creating any object
# whenever we want to create new object, 
# Python first will check string intern pool weather that object already exist are not
# when object already exist in the string intern records then address of existing object will removed