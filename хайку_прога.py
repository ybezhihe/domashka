import random
def two_slog():
    slog = ["Salam" , "Dorad", "Bale", "Bahir", "Shamo", "Harab", "Asan", "Anja", "Pedar", "Dana", "Name", "Deraz", "Asman", "Omid", "Panir", "Ostad", "Nadan", "Anar", "Javan", "Chai", "Hane", "Pornur", "Tape", "Bozorg"]
    return random.choice(slog)

def three_slog():
    slog = ["Miharam", "Gerune", "Pisani", "Miconid", "Setare", "Dvahana", "Daneshgah", "Irani", "Inglisi", "Porsidan", "Amadan", "Meidan", "Siyah", "Hamishe" "Mehraban", "Pushidan", "Parastar", "Zamestan" ]
    return random.choice(slog)
   

def four_slog():
    slog = ["Zaminshenas", "Porsetare", "Nevisande", "Pedarbozorg", "Madarbozorg", "Ordibehesht", "Esterohat", "Bimarestan", "Hamsaye", "Hakestari" ]
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

print (main())
print()

