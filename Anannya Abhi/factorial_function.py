'''
Name: Anannya Abhi
Date: 4.12.24
Python program to define a function to calculate factorial
'''
def factorial(number):
    if number== 1:
        return 1
    else:
        return number*factorial(number-1)
number=int(input("Enter the number:"))
ans=factorial(number)
print(f"The factorial of {number} is: {ans}")
