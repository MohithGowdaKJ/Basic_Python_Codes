#Object.reverse method will reverse the original object
li = [10,20,30,40,50]
print(li)

li.reverse()
print(li)

#list(reversed(object))
li2 = [1,2,3,4,5]
reverse = list(reversed(li2)) #Iterable Object
print(li2) #[1, 2, 3, 4, 5]
print(reverse) #[5, 4, 3, 2, 1]

li3 = [1,2,34,55,42]
reversed_li = list(reversed(li3)) # Creating a new reversed list
print(reversed_li)
li3.reverse() #Reversing a original list
print(li3)