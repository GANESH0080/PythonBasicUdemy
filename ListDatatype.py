values = [2,45,"Ganesh",99,"Salunkhe"]

#Printing 0 and 2 index
print(values[0])
print(values[2])

#Priting last index
print(values[-1])

#Printing index value from 2 to 5 index , 5 will not print
print(values[2 : 5])

#Inserting string at 3rd index
values.insert(3,"Mahadev")
print(values[3])
print(values)

#Adding value at last of List
values.append("End")
print(values)

#Updating value for index 2
values[2] = "GANESH"
print(values)

#Delete specific index
del values[0]
print(values)




