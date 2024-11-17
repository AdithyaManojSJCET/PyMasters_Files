'''Author Anjana Krishna
Date 13 oct 2024
Program for simple calculator'''

operator=input("Enter an operator(+ - / *):")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if operator=="+":
    sum=num1+num2
    print(sum)
elif operator=="-":
    difference=num1-num2
    print(difference)
elif operator=="*":
    product=num1*num2
    print(product)
elif operator=="/":
    division=num1/num2
    print(division)
else:
    print("wrong operator")