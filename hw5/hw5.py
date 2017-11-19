with open("text.txt") as f:
    text = f.read().decode('utf-8').split()
    x = Counter()
    for s in f:
       x[s] += 1
print (x)       
