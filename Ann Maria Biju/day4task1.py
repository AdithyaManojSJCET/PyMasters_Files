'''
name:ann mariya biju
date:14/11/2024
a python program to create a calculator
'''
number1=int(input("enter number 1:"))
number2=int(input("enter number 2:"))
operation=input("enter the operation:")
if operation=="+":
    print(f"{number1}{operation}{number2}:",number1+number2)
elif operation=="-":
    print(f"{number1}{operation}{number2}:",number1-number2)
elif operation=="*":
    print(f"{number1}{operation}{number2}:",number1*number2)
elif operation=="/":
    print(f"{number1}{operation}{number2}:",number1/number2)
elif operation=="//":
    print(f"{number1}{operation}{number2}:",number1//number2)
else:
    print("invalid operator")



