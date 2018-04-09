import re
with open ("fil.txt", encoding="utf-8") as f:
    x = f.read()
    a = re.sub("философ", "астролог", x)
    a = re.sub("Философ","Астролог", x)
    a = re.sub("философия","астрология", x)
    a = re.sub("Философия","Астрология", x)
    a = re.sub("философский","астрологический",x)
    a = re.sub("философии","астрологии",x)
    
print (a)
