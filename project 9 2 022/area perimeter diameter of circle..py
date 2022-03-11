'''
from math import pi
r=eval(input("enter radius of circle:"))
print("area of circle:",pi*r**2)
print("diameter of circle:",r/2)
print("perimeter of circle:",2*pi*r)
'''
#power
import math
pow=1
x,y=eval(input("enter two num:"))
for i in range(1,y+1):                # OR for i in range(y)
    pow=pow*x
print(pow)

#factorial
fact=1
n=eval(input("enter any num:"))
for i in range(1,n+1):
    fact=fact*i
print(fact)




