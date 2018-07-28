import numpy as np
from sys import argv
script,r=argv
pi=np.pi
def calcir(r):
    return 2*pi*r
r=float(r)
c1=calcir(6378)
c2=calcir(3318)
c=calcir(r)
a=(c1+c2)/2
if c>a:
    print "the planet's cir is more close to earth"
else:
    print "the planet's cir is more close to mars"
   
