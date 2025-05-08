count = int(input())
li = []
for i in range(count):
   name = input()
   score = float(input())
   li.append([name,score])
scores = []
for name, score in li:
   scores.append(score)
   scores = list(set(scores))
   scores.sort()
u_name = []
second_smallest = scores[1]
for name, score in li:
   if score == second_smallest:
      u_name.append(name)
u_name.sort()
for name in u_name:
   print(name)