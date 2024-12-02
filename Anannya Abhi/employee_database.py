'''
Name: Anannya Abhi
Date: 2.12.24
Python program to do operations in an employee database
'''
employee={
    "1001":{
        "Name":"Arun","Age":45,"Department":"IT Analyst"
    },
    "1002":{
"Name":"Amy","Age":40,"Department":"HR Head"
    },
    "1003":{
"Name":"Leo","Age":46,"Department":"Software Developer"
    }
}
name=input("Enter the name:")
age=input("Enter the age:")
dept=input("Enter the department:")
employee.update({"1004":{"Name": name, "Age": age, "Department": dept}})
check_id=input("Enter the id to be checked:")
if check_id in employee:
    print(f"The details are: {employee[check_id]}")
delete_id=input("Enter the id of employee to be removed:")
del employee[delete_id]
print(f"The dictionary elements are: {employee}")