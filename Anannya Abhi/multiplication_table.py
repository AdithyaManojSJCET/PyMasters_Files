'''
Name: Anannnya Abhi
Date: 20.11.24
Python program to print multiplication table of a number
'''
number=int(input("Enter the number you want multiplication table of:"))
limit=int(input("Enter the limit till you need the multiplication table:"))
for i in range(0,limit+1):
    print(f"{i}*{number}={i*number}")
