with open ("кр2.txt", encoding="utf-8") as f:
    x = f.read()
    d = x.split("</w>")
    a = len(d)
    

e = open("otvet1.txt", "w", encoding="utf-8")
print (a)
e.close
