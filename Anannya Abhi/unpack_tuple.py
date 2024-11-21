'''
Name: Anannya Abhi
Date: 21.11.24
Python program to unpack elements in a tuple
'''
lst=[]
group=[("Ally","HR Head",120000.00),
          ("Lily","IT Assist",50000.00),
          ("Leo","Technical Analyst",65000.00)
          ]
for employee in group:
    name,post,salary=employee
    lst.append(name)
print(f"The name of employees are:{lst}")

