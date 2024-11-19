'''
Name: Anannnya Abhi
Date: 19.11.24
Python program to get unique value from a list
'''
lst=[]
unique_list=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
    element=int(input("Enter the element:"))
    lst.append(element)
for number in lst:
    if number not in unique_list:
      unique_list.append(number)
print(f"The list without duplicate value is: {unique_list}")
print(f"The original list is: {lst}")