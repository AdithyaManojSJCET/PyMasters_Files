'''Author Anjana Krishna
Date 18 Oct 2024
program to print largest no in a list'''
numbers=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
    number=int(input("Enter the number:"))
    numbers.append(number)
largest=max(numbers)
print("Largest number:",largest)
