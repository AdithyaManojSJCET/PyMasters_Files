'''
Name: Anannya Abhi
Date: 19.11.24
Python program to find max value in a list
'''
lst=[]
limit=int(input("Enter the limit:"))
for i in range(0,limit):
    number=int(input("Enter the number:"))
    lst.append(number)
print(f"The maximum value in the list is : {max(lst)}")
