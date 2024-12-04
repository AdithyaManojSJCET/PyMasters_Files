'''
Name: Anannya Abhi
Date: 4.12.24
Python program to define a function to calculate the area of a circle
'''
def area_of_circle(radius):
    pi=22/7
    area=pi*(radius**2)
    print(f"The area of the circle is: {area}")
radius=float(input('Enter the value for radius:'))
area_of_circle(radius)