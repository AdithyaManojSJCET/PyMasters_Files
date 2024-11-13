'''
Name: Anannnya Abhi
Date: 13.11.24
Python program to create a calculator that operates with 2 numbers
'''
number1=int(input("Enter first number"))
operation=input("What operation do you wanna use?(Use symbol)")
number2=int(input("Enter second number"))
output="Not defined"
if operation=='+':
    output=number1+number2
elif operation=='-':
    output=number1-number2
elif operation=='*' or operation=='x'or operation=='X':
    output=number1*number2
elif operation=='/'and number2!=0:
    output=number1/number2
elif operation=='//'and number2!=0:
    output==number1//number2
elif operation=="^":
    output=number1**number2
elif operation=='%':
    output=number1%number2
else:
    print('Invalid operation')
print(f"{number1}{operation}{number2}={output}")