import random

with open("slog2.txt","r", encoding="utf-8") as f:
    def two_slog():
        text = f.read()
        slog = text.split()
        return random.choice(slog)

    with open("slog3.txt", "r", encoding="utf-8") as a:
        def three_slog():
            mill = a.read()
            slog = mill.split()
            return random.choice(slog)    

            
        with open("slog4.txt", "r", encoding="utf-8") as n:
            def four_slog():
                bom = n.read()
                slog = bom.split()
                return random.choice(slog)


            def punct():
                marks = [".", "،", "!", "؟", "..."]
                return random.choice(marks)

            def str1():
                return two_slog() + " " + three_slog() + punct()

            def str2():
                x = random.randint(2,5)
                if x >= 4:
                    result = four_slog() + " " + three_slog() + punct()
                else:
                    result = two_slog() + " " + three_slog() + " " + two_slog() + punct()
                    return result    



            def str3():
                return three_slog() + " " + two_slog() + punct()

            def main():
                final = str1() + "\n" + str2() + "\n" + str3()
                return final
            print(main())
            print()
            
