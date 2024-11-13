'''
Name: Adithya Manoj
Date: 13/11/2024
Program to create calculator
'''
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))

operation=input("Enter the operation to be expressed( +,-,*,/ ): ")

if operation=='+':
    print("Sum=",num1+num2)
elif operation=='-':
    print("Difference= ",num2-num1)
elif operation=='*':
    print('Multiplication= ',num1*num2)
elif operation=='/':
    print('Quotient= ',num1/num1)
else:
    print("Invalid Input!!")