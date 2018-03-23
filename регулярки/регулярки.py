import re

text = open("re.txt")
x = text.read()
text.close()
a = re.findall("вып[а-я]+", x)
print (a)
