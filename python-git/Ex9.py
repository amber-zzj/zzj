from sys import argv
script,filename=argv
text=open(filename,"r")
s=text.read()
print s
filename=raw_input("filename is: ")
text1=open(filename,"a+")
text1.write(s)
text1.seek(0)
s1=text1.read()
print s1

