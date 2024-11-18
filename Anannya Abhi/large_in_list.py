'''
Name: Anannnya Abhi
Date: 18.11.24
Python program to find largest number in a list;to sort list in ascending order;count occurence of an element
'''
number=[1,2,13,76,99,28,27,54,77,27,11,23,838]
number.sort()
total_count=number.count(27)
large=number[-1]
print(f"The largest number in the list is:{large}")
print(f"The list sorted in ascending order id: {number}")
print(f"The occurance of 27 is:{total_count}")



