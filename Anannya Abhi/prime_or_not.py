'''
Name: Anannnya Abhi
Date: 20.11.24
Python program to check if a number is prime number using for loop
'''
number=int(input("Enter a number:"))
Prime=True
for i in range(2,(number//2)+1):
  if number%i==0:
     Prime=False
if number<2:
    print('Invalid entry')
elif Prime:
     print("The number is prime.")
else:
    print("The number is composite")