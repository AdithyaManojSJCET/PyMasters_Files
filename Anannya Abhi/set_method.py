'''
Name: Anannya Abhi
Date: 27.11.24
Python program using set functions
'''
fruits={"Avocado","Apple","Mango","Orange","Cucumber"}
veg_fruits={"Avocado","Tomato","Cucumber","Pumpkin"}
print(f"Union of the given sets are: {fruits | veg_fruits}")
print(f"Intersection of the given sets are: {fruits & veg_fruits} ")
print(f"Difference of 1st set-2nd set is: {fruits-veg_fruits}  &\nof 2nd set-1st set is: {veg_fruits-fruits}")