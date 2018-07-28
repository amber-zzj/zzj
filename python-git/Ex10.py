import numpy as np
pi=np.pi
def calcir(r):
    return 2*pi*r
def calsur(r):
    return 4*pi*r*r
r1=6378
r2=3378
l1=calcir(r1)
s1=calsur(r1)
l2=calcir(r2)
s2=calsur(r2)
print "earth\n\t*circumference of the equater is \t",l1,"Km\n\t*surface is \t",s1,"Km^2"
print "mars\n\t*circumference of the equater is \t",l2,"Km\n\t*surface is \t",s2,"Km^2"

