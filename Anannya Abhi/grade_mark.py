'''
Name: Anannya Abhi
Date: 12.11.24
Python program to grade a student based on their marks
'''
mark=int(input("Enter your mark:"))
if mark>=90:
    print("Your grade is'A'")
elif(mark>=80 and mark<90):
    print("Your grade is 'B'")
elif mark>=70 and mark<80:
    print("Your grade is'C'")
else:
    print("Your grade is'D'")
