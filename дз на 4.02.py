x = input()
ch == 0
def whole_file(x):
    with open (x, encoding='utf-8') as  f:
    text = f.read()
    text = text.replace('-', '')  
    text = text.replace(',', '').replace('.', '')  
    text = text.lower()  
    words = text.split()
    return words
def ed_words():
    for y in words:
        y == words[1:-2]
        if y = "ed":
            ch += 1
    return y
print (ch)


    
