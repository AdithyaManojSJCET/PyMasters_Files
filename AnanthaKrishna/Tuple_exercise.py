"""
Auther : Ananthakrishnan K V
Date : 26-11-2024

1) Write a program to access the third element of a tuple.

2) Write a program to check if an element (e.g., 4) exists in a tuple.

3) Write a program to print each element in a tuple
"""
#1
t = (1,2,3,4,5,6)
print(f"Tuple = {t}")
print(f"Third element in tuple {t[2]}")

#2
print(4 in t)

#3
print(f"Each element in the tuple are")
for i in t:
    print(t[i-1],"\t",end='')