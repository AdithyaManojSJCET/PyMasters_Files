'''Author Anjana Krishna
 Day 16 Python Challenge
 Program with dictionary
 '''
 
 #program1
Details={"name":"Raju","age":25,"city":"Delhi"}

print(Details)
print(Details.get("name"))
print(Details.get("age"))
print(Details.get("city"))


#program2
Items={"fruit":"apple","colour":"red"}
print(Items)
(Items.update({"price":10}))
print(Items)


#program3
info={"name":"Pooja","age":30,"job":"doctor"}
info.pop("job")
print(info)

