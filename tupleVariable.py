valuestuple = (5, 66, "Ganesh", 87, "Salunkhe")

#Printing 1 index
print(valuestuple[1])

#Printing last index value
print(valuestuple[-1])

#Printing index value from 2 to 5 index , 5 will not print
print(valuestuple[2 : 5])

#It will not work because Tuple is Imutable
#valuestuple.insert(3,"Mahadev")
#valuestuple.append("End")
#valuestuple[2] = "GANESH"
# del valuestuple[0]