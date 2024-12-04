'''
Name: Anannya Abhi
Date: 4.12.24
Python program to define a function to check if a number is even or odd
'''
def even_or_odd(input_number):
    if input_number%2==0:
        print(f"The given number {input_number} is EVEN")
    else:
        print(f"The given number {input_number} is ODD")
input_number=int(input("Enter a number:"))
even_or_odd(input_number)