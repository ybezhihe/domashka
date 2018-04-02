import re

text = open("эйнштейн.html")
x = text.read()
text.close()
z = re.findall("^Научная сфера ([а-я]+)+$", x)

print(z)
