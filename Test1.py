Hrac1Skore = 0
Hrac2Skore = 0
VzalenostHrac1 = 10
VzalenostHrac2 = 0


def pocetb():
    global Hrac1Skore
    global Hrac2Skore
    if Vzalenost > 10:
        Hrac1Skore += 1
        print(f"Hráč 1 má skóre:{Hrac1Skore} a Hráč 2 má skóre:{Hrac2Skore} a vzdálenost je {Vzalenost}")
    elif Vzalenost < 0:
        Hrac2Skore += 1
        print(f"Hráč 1 má skóre:{Hrac1Skore} a Hráč 2 má skóre:{Hrac2Skore} a vzdálenost je {Vzalenost}")

def vypocetBodu(x):
    x += 1
    print(f"Hráč 1 má skóre:{Hrac1Skore} a Hráč 2 má skóre:{Hrac2Skore} a vzdálenost je {Vzalenost}")
    return x

if __name__ == "__main__":

    while Hrac1Skore < 10 and Hrac2Skore < 10:
        Vzalenost = int(input("Vzdálenost je:"))


        if Vzalenost > VzalenostHrac1:
            Hrac1Skore = vypocetBodu(Hrac1Skore)
        elif Vzalenost < VzalenostHrac2:
            Hrac2Skore = vypocetBodu(Hrac2Skore)