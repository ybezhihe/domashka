word = list(input("Введите слово: "))
x = len(word)
a = word.pop ()
word1 = [a] + [word]
print (word1)
for i in range (x-1):
    a = word.pop ()
    word1 = [a] + [word1]
    print (word1)
