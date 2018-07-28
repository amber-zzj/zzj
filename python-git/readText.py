from sys import argv
script,mytest=argv
text=open(mytest)
print "The content of %s:" % mytest
print text.read()
