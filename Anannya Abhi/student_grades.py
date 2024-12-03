'''
Name: Anannya Abhi
Date: 3.12.24
Python program to do operations in a student grade dictionary
'''
student_grade={
    "Arya":[23,45,34,38],
    "Daya":[44,23,37,45],
    "Alen":[44,36,39,45],
    "Tio":[47,45,36,33]
}
print(f"The og dictionary is: {student_grade}")
student_grade.update({"Denny":[35,39,41,44]})
student_grade["Tio"][-1]=45
values=student_grade.keys()
for student,grades in student_grade.items():
    total= sum(grades)
    avg=total/len(grades)
    print(f"Average of grade of {student} is: {avg}")