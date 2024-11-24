'''
Name: Anannya Abhi
Date: 24.11.24
Python program to access the third element of a tuple
'''
length=int(input("Enter the lenght of the tuple(length>=3): "))
element=[]
for i in range(0,length):
    value=input("Enter the element: ")
    element.append(value)
entries=tuple(element)
print(f"The third element in the tuple is: {element[2]}")

