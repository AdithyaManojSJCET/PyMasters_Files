"""
Auther : Ananthakrishnan K V
Date : 26-11-2024
1) Write a Python program to convert list to tuple

2)Write a Python program to find the number of occurrences of an element

3) Write a Python program to find the max and min values in a tuple
"""
lst = ['apple','orange','apple',1,2,3,'banana','apple']

#1)convert list to tuple
converted_list = tuple(lst)
print(f" Tuple converted list = {converted_list}")

#2)number of occurrences of an element
print(f"Occurrence of apple in the tuple is {converted_list.count('apple')}")

#3)max and min values in a tuple
t=(1,2,3,4,5,6,7,8,9)
print(f"Tuple:{t}")
maximum=max(t)
minimum=min(t)
print(f"Maximum value in the tuple:{maximum}")
print(f"Minimum value in the tuple:{minimum}")
