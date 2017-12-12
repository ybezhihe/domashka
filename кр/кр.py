with open("C:/Users/student/Desktop/Extinct_languages.tsv" , "r", encoding = "utf-8") as f:
    for x in f:
        x = str.split("\n")
        if int(len(x)) > 35:
            print (x)   
f.close()
