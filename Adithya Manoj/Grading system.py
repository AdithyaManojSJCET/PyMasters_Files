'''
Author: Adithya Manoj
Date: 12/11/2024
'''
marks=int(input("Enter Your Marks: "))

if marks>=90:
    print("Grade: A")
elif marks>=80:
    print("Grade: B")
elif marks>=70:
    print("Grade: C")
elif marks<60:
    print("Grade: D")
else:
    print("Invaild Grade!")