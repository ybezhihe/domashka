with open("C:/Users/student/Desktop/Extinct_languages.tsv" , "r", encoding = "utf-8") as f:
    k = 0
    for i in f:
        x = str.split(" ")
        if str(x) == "Critically":
            k = k + 1
f.close()
print (k)
