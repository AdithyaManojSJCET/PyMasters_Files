'''
Name: Anannya Abhi
Date: 5.12.24
Python program to define a function to calculate compound interst
'''
def compound_interest():
    principal_amount=float(input("Enter the Principal amount:"))
    rate_of_interest=float(input("Enter the rate of intrest:"))
    time_period=float(input("Enter the time period:"))
    if principal_amount and rate_of_interest and time_period >0:
        total_amount=principal_amount*((1+(rate_of_interest/100))**time_period)
        print(f"The final amount after {time_period} years with rate of interest {rate_of_interest} is: {total_amount} ")
    else:
        print("Enter valid values!")
compound_interest()