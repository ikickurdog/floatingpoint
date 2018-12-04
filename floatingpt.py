import math
from math import log
a = 1 #2/math.pi to see missing outputs, 1/math.pi for repeated inputs
b= 2**-53 #2**-53 to see missing outputs, 2**-54 for repeated inputs
print(b)
c = [a,a+b, a+2*b,a+3*b,a+4*b,a+5*b,a+6*b,a+7*b,a+8*b,a+9*b]  #input
print(c)
d = [log(a+b),log(a+b), log(a+2*b),log(a+3*b),log(a+4*b),log(a+5*b),log(a+6*b),log(a+7*b),log(a+8*b),log(a+9*b)] #output 
print(d)
e = [d[0]-d[1],d[1]-d[2],d[2]-d[3],d[3]-d[4],d[4]-d[5],d[5]-d[6],d[6]-d[7],d[7]-d[8],d[8]-d[9]] #spacing between outputs
print(e)
