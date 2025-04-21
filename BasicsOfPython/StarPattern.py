rows = 4
col = 5

# Rectangle Pattern
for i in range(rows):
    for j in range(col):
        print("*",end="")
    print()

# Increasing Pattern[Right Angle Triangle]
for i in range(rows):
    for j in range(i):
        print("*",end="")
    print()
print()

# Decreasing Pattern
for i in range(rows):
    for j in range(i,rows):
        print("*",end="")
    print()
print()

# Right 
for i in range(rows):
    for j in range(i):
        print("*",end="")
    print()
for i in range(rows):
    for j in range(i,rows-2):
        print("*",end="")
    print()
print()

# Butterfly Pattern
for i in range(rows):
    for j in range(i+1):
        print("*",end="")
    for j in range(i,rows-1):
        print(" ",end="")
    for j in range(i,rows-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(rows):
    for j in range(i,rows-1):
        print("*",end="")
    for j in range(i+1):
        print(" ",end="")
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,rows-1):
        print("*",end="")
    print()
print()

# Daimond Shape Pattern
for i in range(rows):
    for j in range(i,rows-1):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(1,rows):
    for j in range(i):
        print(" ",end="")
    for j in range(i,rows-1):
        print("*",end="")
    for j in range(i,rows):
        print("*",end="")
    print()
