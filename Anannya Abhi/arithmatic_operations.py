'''
Name: Anannnya Abhi
Date: 11.11.24
Python program to perform arithmetic operations
'''

"""Simple arithematic operations like
addition,subtraction,multiplication,division,modulus,exponential,and floor division are performed"""
num1=int(input("Enter a number:"))
num2=int(input("Enter a second number:"))
sum=num1+num2
differ=num1-num2
product=num1*num2
quotient=num1/num2
modulus=num1%num2
power=num1**num2
int_floor_div=num1//num2
print(f"Sum={sum}\nDifference={differ}\nProduct={product}\nQuotient={quotient}\nFloor dividion={int_floor_div}\nModulus={modulus}"
      f"\nExponent(power)={power}")