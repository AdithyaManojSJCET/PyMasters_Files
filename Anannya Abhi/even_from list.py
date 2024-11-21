'''
Name: Anannya Abhi
Date: 20.11.24
Python program to find even numbers from a list using for loop
'''
limit=int(input("Enter the limit:"))
lst=[]
for i in range(0,limit):
    element=int(input("Enter the element:"))
    lst.append(element)
for i in lst:
    if i%2==0:
        print(f"The given number {i} is even.")
    else:
        print(f"The given number {i} is odd.")




