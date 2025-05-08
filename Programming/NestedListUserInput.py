# TODO: Prompt the user to enter a number and store it in num
num = int(input())
number = num
# TODO: Use a while loop to iterate through each digit to find the first multiple of 3
isMultiple = 0
# TODO: Use a break statement to exit the loop once a multiple of 3 is found
while(num > 0):
   digit = num % 10
   if(digit % 3 == 0):
      isMultiple = digit
      break
   num = num // 10      
# TODO: Print the result
if (isMultiple == 0):
   print(f"No multiple of 3 found in {number}.")
else:
   print(f"The last multiple of 3 in {number} is {isMultiple}.")
