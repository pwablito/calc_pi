#!/usr/bin/python
#from decimal import *
#precision = 11
#getcontext().prec = precision
n = 1000000
def f(x):
    return (1-(float(x)**2))**float(0.5)
val = 0
for i in range(n):
    i = i+1
    val = val+f(float(i)/float(n))
val = val*2
pi = (float(2)/n)*(float(1)+val)
print pi
