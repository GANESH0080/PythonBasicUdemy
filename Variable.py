# Variable declaration and print
from ftplib import print_line

#Example 1
a = 3
print(a)
print(a)
print_line(a)

#Example 2
str = "hello world"
print_line(str)


#Example 3
g, b, c, d = 5,5.9,"Ganesh",99
print(g)
print(b)
print(c)
print(d)

#Printing variable with string
print("{} {} {}".format("Value of G is :", g, "and that is correct"))
print("{} {} {}".format("Value of B is :", b, "and that is correct"))
print("{} {}".format("Value of C is :", c))
print("{} {}".format("Value of D is :", d))
print("Value of GGGG is :" +g)


#Printing datatype of variable
print(type(g))
print(type(b))
print(type(c))
print(type(d))