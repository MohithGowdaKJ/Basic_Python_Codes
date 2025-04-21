li = [1, 2, 3, 4, 5]
'''print(li)
sq_li = []
for i in li:
    sq_li.append(i**2)
print(sq_li)
'''
# expression(i+2) for control_variable(i) in iterable_object if condition(if required)
new_ele = [i for i in li]
print(new_ele)

sq_ele = [i**2 for i in li]
print(sq_ele)

sum_ele = [i+2 for i in li]
print(sum_ele)

# When we have only if condition then we write it after for loop
even_ele = [i for i in li if i%2 == 0 ]
print(even_ele)

# When we have both if and else condition we write it before for loop
even_odd = ['even' if i%2==0 else 'Odd' for i in li]
print(even_odd)

#Mulitple Loops inside list Comprehension
li2 = [[10,20],[30,40],[50,60]]
new_ele = [j for i in li2 for j in i]
print(new_ele)