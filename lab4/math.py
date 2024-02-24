#ex1
import math

a= int(input())

print(float((a/180)*math.pi))
#ex2
import math

h = int(input())

b1 = int(input())
b2 = int(input())

print(float(h*(b1+b2)/2))
#ex3
import math
print('Input number of sides:')
n = int(input())
print('Input the length of a side:')
s = int(input())
p = n * s
a = 2 * math.tan((180/n) * (math.pi/180))
b = s / a
A = n*s*b * (1/2)
print('The area of the polygon is:', int(A))

#ex4
import math
h = int(input())
l = int(input())

print(float(h*l))
