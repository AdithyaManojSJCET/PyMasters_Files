'''
Name: Anannya Abhi
Date: 28.11.24
Python program using set functions
'''
element=["Mango"]
fruits=set(element)
fruits.add("Pumpkin")
print(f"The set after adding elemnet is: {fruits}")
fruits.update(["Orange","Avocado"])
print(f"The set after updating is:{fruits}")
fruits.discard("Orange")
print(f"The set after discarding orange is:{fruits}")
fruits.pop()
print( f"The set after using pop() is:{fruits}")
fruits.clear()
print(f"The set after using clear() is:{fruits}")

