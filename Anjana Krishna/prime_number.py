'''Author Anjana Krishna
  Day 8 Python Challenge
  Python program to find prime number     using for loop
  '''
  number=int(input("Enter a number:"))
  for num in range(2,number):
   if number%num==0:
   	print(" The number is not prime")
  else:
   print("The number is prime")
   
   