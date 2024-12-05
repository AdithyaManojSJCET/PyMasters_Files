'''
Name: Anannya Abhi
Date: 5.12.24
Python program to define a function to convert temperature
'''
def temperature_convert(temperature):
    degree=input("Is this in (C)elsius or (F)ahrenheit? ")
    if degree=="C" or degree=="c" or degree=="F" or degree=="f":
        if degree=="C" or degree=="c":
            fahrenheit=((9/5)*temperature)+32
            print(temperature,"Celsius is",fahrenheit,"Fahrenheit." )
        else:
            celsius=(5/9)*(temperature-32)
            print(temperature,"Fahrenheit is",celsius,"Celsius")
    else:
        print("Invalid input for celsius or fahrenheit")
temperature=float(input("Enter temperature:"))
temperature_convert(temperature)