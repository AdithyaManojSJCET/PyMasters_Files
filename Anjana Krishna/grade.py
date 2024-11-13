'''Author Anjana Krishna
date 12 oct 2024
Program to grade a student based on their marks'''
mark=int(input("Enter your mark:"))

if mark>=90:
    print(f"Your grade is A")
elif mark>=80:
    print("Your grade is B")
elif mark>=70:
    print("Your grade is C")
else:
    print("YOur grade is D")
