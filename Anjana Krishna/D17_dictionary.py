'''Author Anjana Krishna
  Day 17 Python Challenge
  Program with dictionary
'''
#length of dictionary
my_dictionary={"name":"Priya",
"age":30}
length=len(my_dictionary)
print("Length of dictionary:",length)

#to retrieve items,values,keys
print(my_dictionary.keys())
print(my_dictionary.items())
print(my_dictionary.values())


#to update
my_dictionary.update({"age":29})
print(my_dictionary)