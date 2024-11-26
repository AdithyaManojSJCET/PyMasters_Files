"""
Auther : Ananthakrishnan K V
Date : 26-11-2024
Print the multiplication table of a number.
"""

n = int(input("Enter a number: "))
for i in range(1,11)  :
    ans=n*i
    print(f"{n}\tx\t{i}\t=\t{ans}")