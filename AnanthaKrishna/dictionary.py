'''Auther : Ananthakrishnan K V
Date : 1-12-2024
1.)Write a program to create a dictionary with the following key-value pairs:

{'name': 'Raju', 'age': 25, 'city': 'Delhi'}.

Access and print the value of the key name.

2) Create a dictionary with the following:

{'fruit': 'apple', 'color': 'red'}.

Add a new key-value pair: 'price': 10.

3) Remove a Key from a Dictionary

Create a dictionary: {'name': 'Pooja', 'age': 30, 'job': 'Doctor'}.

Remove the key job from the dictionary.
'''
#1
my_dict = {'name': 'Raju',
           'age': 25,
           'city': 'Delhi'}
print(my_dict['name'],my_dict['age'],my_dict['city'])

#2
new_dict = {'fruit': 'apple',
            'color': 'red'}
new_dict['price'] = 10
print(new_dict)

#3
dict = {'name': 'Pooja',
        'age': 30,
        'job': 'Doctor'}
del dict['job']
print(dict)