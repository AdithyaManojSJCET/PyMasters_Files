'''
Name: Anannya Abhi
Date: 19.11.24
Python program to get the frequency of elements in list
'''
list=[]
num=int(input("Enter the number of list elements: "))
for i in range(num):
    element=int(input("Enter the element:"))
    list.append(element)
    print(f"The frequency of {element} is : {list.count(element)}")
