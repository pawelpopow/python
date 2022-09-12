import random

numberofnumbers = int(input("Podaj ilość typowanych liczb: "))
maxnumber = int(input("Podaj maksymalna losowa liczbe: "))

if __name__ == '__main__':
    types = set()
    number = []
    hit = set(number) & types

    if hit:
        print("\n Ilosc trafien: %s" % len(hit))
        print("Trafione liczby: ", hit)
    else:
        print("Brak trafien. Sprobuj jeszcze raz!")