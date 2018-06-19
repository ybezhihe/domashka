import re
encoding = "utf-8"
text1 =open(r"C:\Users\student\Desktop\news\_itartass1.xhtml")
x = text1.read()
text1.close()
a = re.findall("[А-Я]+[А-Я]+*", x)

text2 = open(r"C:\Users\student\Desktop\news\_itartass2.xhtml")
x2 = text2.read()
text2.close()
a2 = re.findall("[А-Я]+[А-Я]+*", x2)

text3 =open(r"C:\Users\student\Desktop\news\_itartass3.xhtml")
x3 = text3.read()
text3.close()
a3 = re.findall("[А-Я]+[А-Я]+*", x3)

text4 = open(r"C:\Users\student\Desktop\news\_itartass4.xhtml")
x4 = text4.read()
text4.close()
a4 = re.findall("[А-Я]+[А-Я]+*", x4)

text5 = open(r"C:\Users\student\Desktop\news\_itartass5.xhtml")
x5 = text5.read()
text5.close()
a5 = re.findall("[А-Я]+[А-Я]+*", x5)

text6 = open(r"C:\Users\student\Desktop\news\_rbk2.xhtml")
x6 = text6.read()
text6.close()
a6 = re.findall("[А-Я]+[А-Я]+*", x6)

text7 = open(r"C:\Users\student\Desktop\news\_rbk3.xhtml")
x7 = text7.read()
text7.close()
a7 = re.findall("[А-Я]+[А-Я]+*", x7)

text8 = open(r"C:\Users\student\Desktop\news\_rbk4.xhtml")
x8 = text8.read()
text8.close()
a8 = re.findall("[А-Я]+[А-Я]+*", x8)

text9 = open(r"C:\Users\student\Desktop\news\_rbk6.xhtml")
x9 = text9.read()
text9.close()
a9 = re.findall("[А-Я]+[А-Я]+*", x9)

text10 = open(r"C:\Users\student\Desktop\news\_rbk7.xhtml")
x10 = text10.read()
text10.close()
a10 = re.findall("[А-Я]+[А-Я]+*", x10)

text11 = open(r"C:\Users\student\Desktop\news\_rian1.xhtml")
x11 = text11.read()
text11.close()
a11 = re.findall("[А-Я]+[А-Я]+*", x11)

text12 = open(r"C:\Users\student\Desktop\news\_rian2.xhtml")
x12 = text12.read()
text12.close()
a12 = re.findall("[А-Я]+[А-Я]+*", x12)

text13 = open(r"C:\Users\student\Desktop\news\_rian3.xhtml")
x13 = text13.read()
text13.close()
a13 = re.findall("[А-Я]+[А-Я]+*", x13)

text14 = open(r"C:\Users\student\Desktop\news\_rian5.xhtml")
x14 = text14.read()
text14.close()
a14 = re.findall("[А-Я]+[А-Я]+*", x14)

l = a + a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11 + a12 + a13 + a14
print (l)

from collections import Counter
l = [a, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14]
d = Counter(l)

with open ("экзамен2.csv", "w", encoding = "utf-8") as f:
    table = {d}
    

    










