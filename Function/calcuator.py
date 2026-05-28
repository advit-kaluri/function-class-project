def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b


print("enter the numbers to calculate ")
num1 = int(input("frist number :"))
num2 = int(input("second number :"))


print("\n Enter 1 for Addition \n Enter 2 for Subtraction \n Enter 3 for Multiplication \n Enter 4 for Division : ")

choice = input("Enter your choice of operation : ")

if choice=="1":
    print("Result : ", add(num1, num2))

elif choice=="2":
    print("Result : ", sub(num1, num2)) 


elif choice=="3":
    print("Result : ", mul(num1, num2)) 


elif choice=="4":
    print("Result : ", div(num1, num2)) 
        


    


    









    