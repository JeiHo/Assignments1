print("Jei Ho")
print("9/12/19")
print("Math Problem Assignment")
print("Sources: none")
print("OMH\n")

#problem 1
import sys
import math
#t = float(sys.argv[1])
#v = float(sys.argv[2])

#w = 35.74 + 0.6215t + (0.4275t - 35.75)v**0.16
#print(w)

#problem 2
#x = float(sys.argv[1])
#y = float(sys.argv[2])
#z = float(sys.argv[3])
#result = x<y<z or x>y>z
#print(result)

#problem 3
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])
z = math.floor((14-m)/12)

x = math.floor(y + (y/4) - (y/100) + (y/400))
m = m - 2 +12*z
d = math.floor((d + x + ((31*m)/12))%7)
print(d)
