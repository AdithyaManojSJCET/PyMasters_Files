"""
Auther : Ananthakrishnan K V
Date : 26-11-2024
Check if a number is prime using a for loop.
"""
n = int(input("Enter a number: "))

isPrime=True
for i in range(2,n//2+1):
    if n%i==0:
        isPrime=False
        break

if isPrime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is Not a prime number")
