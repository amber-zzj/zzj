from sys import argv
script,textfile=argv
text=open(textfile,"w")
line1="zhd is a little pig!"
line2="I love this pig!"
line3="And this pig is very cute!"
text.write(line1)
text.write("\n")
text.write(line2)
text.write("\n")
text.write(line3)
text.write("\n")
text.close()
