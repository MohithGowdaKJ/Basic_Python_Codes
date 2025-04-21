# Write a program to print all even index element
li = [10, 20, 30, 40, 50]
for idx, ele in enumerate(li): # Enumerate => if we want to work with both index and element
    print(f"Index of {ele} is {idx}")

for idx,ele in enumerate(li,start=1): # Start will specify from where the index should start
    if idx % 2 == 0:
        print(ele,end=" ")