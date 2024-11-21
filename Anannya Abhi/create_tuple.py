'''
Name: Anannya Abhi
Date: 21.11.24
Python program to create and display a tuple
'''
lst=[]
number_of_elements=int(input("Enter the number of elements:"))
for i in range(0,number_of_elements):
    value=int(input("Enter the value:"))
    lst.append(value)
print(f"The tuple is:{lst}")
