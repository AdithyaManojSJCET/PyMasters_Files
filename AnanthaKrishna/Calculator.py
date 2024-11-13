'''Auther : Ananthakrishnan K V
Date : 13-11-2024
 Calculator
'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter an operator(+,-,*,/)")

if operator== '+':
    print(f"{num1} + {num2} = {num1+num2}")
elif operator=='-':
    print(f"{num1} - {num2} = {num1- num2}")
elif operator=='*':
    print(f"{num1} * {num2} = {num1* num2}")
elif operator=='/':
    print(f"{num1} / {num2} = {num1/ num2}")
else:
    print("invalid input")

