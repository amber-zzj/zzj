import numpy as np
from sys import argv
script,r=argv
print "The script is called:",script
print "r is:",r
r=float(r)
pi=np.pi
l =2*pi*r
s=4*pi*r*r
print "the cir of the earth equater is",l,"Km"
print "the cir of the earth equater is %s"%l,"Km"
print "the cir of the earth equater is %r"%l,"Km"
print "earth\n\t*circumference of the equater is \t",l,"Km\n\t*surface is \t",s,"Km^2"
print "earth\n\t*circumference of the equater is \t %s Km\n\t*surface is \t\t\t\t %s Km^2"%(l,s)
r=float(raw_input("Please cin another r:"))
pi=np.pi
l =2*pi*r
s=4*pi*r*r
print "the cir of the earth equater is",l,"Km"
print "the cir of the earth equater is %s"%l,"Km"
print "the cir of the earth equater is %r"%l,"Km"
print "earth\n\t*circumference of the equater is \t",l,"Km\n\t*surface is \t",s,"Km^2"
print "earth\n\t*circumference of the equater is \t %s Km\n\t*surface is \t\t\t\t %s Km^2"%(l,s)
