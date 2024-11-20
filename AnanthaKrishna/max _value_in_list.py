'''Auther : Ananthakrishnan K V
Date : 20-11-2024
Write a  Python program to find the max in a list
'''

list=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
    number=int(input("Enter the number:"))
    list.append(number)
    max_value=max(list)
print(f"The maximum value in the list is : {max_value}")