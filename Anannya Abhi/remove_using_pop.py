'''
Name: Anannya Abhi
Date: 1.12.24
Python program to remove element using pop() in dictionary
'''
values={'fruit': 'apple', 'color': 'red','name': 'Raju','age': 25,'city': 'Delhi'}
print(f'The og dictionary is: {values}')
values.pop("name")
print(f"The dictionary after using pop() is: {values}")