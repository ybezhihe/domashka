with open("угадай слово.csv", "w", encoding="utf-8") as f:
    f.write("Finding,V1,V2,V3\n")
    f.write("заяц,пугливый,серый,беляк\n")


def find_word(x):
    d = {}
    with open("угадай слово.csv", encoding = "utf-8") as f:
        z = d[0]
        e = len(z)
        print(d[1],"."*e)
        w = input()
        if w == z:
            print("Красавчик!")
        else:
            print(d[2],"."*e)
            y = input()
            if y == z:
                print("Молодец!")
            else:
                print(d[3], "."*e)
                c = input()
                if c==z:
                    print("Хорошо!")
                else:
                    print("Сегодня явно не твой день...")
    return d
                    
    






    
