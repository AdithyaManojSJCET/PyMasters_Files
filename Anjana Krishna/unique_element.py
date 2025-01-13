'''Author Anjana Krishna
   Program to find unique elements from a list'''

original_list=[1,2,3,3,4]
unique_element=[]
for number in  original_list:
      if number not in unique_element:
          unique_element.append(number)
print("Unique value:",unique_element)
          
      
