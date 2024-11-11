'''Auther : ananthakrishnan K V
Date : 11-11-2024
 Program to perform all arithmetic operations
'''


num1 = int(input("Enter an integer number: "))
num2 = int(input("Enter a second integer number "))

#Addition
a = num1+num2
#Substraction
s = num1-num2
#Division
d = num1/num2
#Multiplication
m = num1*num2
#Modulus
MOD = num1%num2
#Floor division
floor = num1//num2
#Exponential
expo = num1**num2

print(f"{num1}+{num2}={a}")
print(f"{num1}-{num2}={s}")
print(f"{num1}/{num2}={d}")
print(f"{num1}*{num2}={m}")
print(f"{num1}%{num2}={MOD}")
print(f"{num1}//{num2}={floor}")
print(f"{num1}**{num2}={expo}")