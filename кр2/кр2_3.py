import re
with open("кр2.txt", encoding="utf-8") as f:
    x = f.read()

z = open ("otvet3.cvs", "w", encoding="utf-8")
print(x.split("\w"))
s = re.findall("type=\"f.h[a-z]+\"", x)
print (s)
z.close
