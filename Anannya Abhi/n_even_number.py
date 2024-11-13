'''
Name: Anannnya Abhi
Date: 13.11.24
Python program to generate n even numbers
'''
limit=int(input("Enter value for n:"))
print(f"{limit} even numbers are:")
even_num=-2
even_num1=2
if limit>=0:
 for i in range(0,limit):
  even_num=even_num+2
  print(even_num,end=" ")
else:
    for i in range(limit,0):
        even_num1 = even_num1 - 2
        print(even_num1, end=" ")
