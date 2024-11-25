'''
Name: Anannya Abhi
Date: 25.11.24
Python program to find the number of occurrences of an element
'''
length=int(input("Enter the length of the list:"))
lst=[]
for i in range(0,length):
    value=input("Enter the element: ")
    lst.append(value)
check=input("Enter the value for which occurrence is to be found:")
print(f"The occurrence of {check} is: {lst.count(check)}")


