print("Jei Ho")
print("9/10/2019")
print("HW: Basic Formulas Math Practice")
print("Sources: None")
print("OMH")

#problem 1
#Problem: the formula is not followed as r**2 is not being divided; instead, r is divided first and then multiplied.
#2 ways to adjust: 1. put parenthesis around radius*radius, 2. divide by radius**2 instead

#problem 2
import math
import sys

angle = int(sys.argv[1])
answer = (math.sin(angle)**2) + (math.cos(angle)**2)
print(answer)

#the value is not always 1 because sin, cos can only approximate to a certain digit and does not round up nor round down

#problem 3
x = int(input("x-coordinate: "))
y = int(input("y-coordinate: "))
#distance formula
distance = math.sqrt((x**2)+(y**2))
print(distance)