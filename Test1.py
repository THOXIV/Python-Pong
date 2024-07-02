Hrac1Skore = 0
Hrac2Skore = 0
VzalenostHrac1 = 10
VzalenostHrac2 = 0
Vzalenost = 5

def vypocetBodu(x):
    x += 1
    print(f"Hráč 1 má skóre:{Hrac1Skore} a Hráč 2 má skóre:{Hrac2Skore} a vzdálenost je {Vzalenost}")
    return x

def resetVzdalenost(V=5):
    print(f"Vzdálenost je {V}")
    return V

if __name__ == "__main__":

    while Hrac1Skore < 10 and Hrac2Skore < 10:
        Vzalenost += int(input(f"Vzdálenost je:{Vzalenost}+"))
        if Vzalenost > VzalenostHrac1:
            Hrac1Skore = vypocetBodu(Hrac1Skore)
            Vzalenost = resetVzdalenost(5)
        elif Vzalenost < VzalenostHrac2:
            Hrac2Skore = vypocetBodu(Hrac2Skore)
            Vzalenost = resetVzdalenost(5)


