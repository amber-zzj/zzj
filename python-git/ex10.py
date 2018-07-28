from sys import argv
mytest=raw_input("please input the name of txt: ")
text=open(mytest)
print "The content of %s:" % mytest
print text.read()
