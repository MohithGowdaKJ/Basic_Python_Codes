def checkAge(age):
    if(age > 18):
        print("Age is greater than 18")
    else:
        print("Age is less than 18")
checkAge(21)  

def ageCheck(age):
    if(age < 18 ):
        print("Child")
    if(age > 18 and age < 65):
        print("Adult")
    else:
        print("SeniorCitizen")   

ageCheck(int(input("Enter a Age")))     