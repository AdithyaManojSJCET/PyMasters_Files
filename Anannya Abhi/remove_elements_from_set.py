'''
Name: Anannya Abhi
Date: 26.11.24
Python program to remove elements from a set
'''
fruits={"Orange",}
limit=int(input("Enter the limit:"))
for i in range(0,limit):
    value=input("Enter the element:")
    fruits.add(value)
print(f"The set elements are: {fruits}")
delete=input("Enter the value to be removed:")
fruits.discard(delete)
print(f"The updated set is: {fruits}")