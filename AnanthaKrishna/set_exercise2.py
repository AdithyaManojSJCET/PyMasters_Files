'''Auther : Ananthakrishnan K V
Date : 1-12-2024
'''


fruits = {'apple','banana','orange'}
fruits.add('cherry')
print(fruits)

fruits.update(['kiwi'])
print(fruits)

#discard doesn't show any error even if the value is not in the set
fruits.discard('nuts')
print(fruits)

#remove will show errors
fruits.remove('apple')
print(fruits)

fruits.pop()
print(fruits)

fruits.clear()
print(fruits)