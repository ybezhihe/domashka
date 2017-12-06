with open("C:\Users\пп\Desktop\прога\питон\hw5\txt.txt",encoding="utf-8") as f :
    text = f.read().split()
    x = Counter()
    for s in f:
       x[s] += 1
print (x)       
