import random

numberofnumbers = int(input("Podaj ilość typowanych liczb: "))
maxnumber = int(input("Podaj maksymalna losowa liczbe: "))

if __name__ == '__main__':
    print("Wytypuj %s z %s liczb: " % (numberofnumbers, maxnumber))
    types = set()
    i = 0
    while i < numberofnumbers:
        type = input("Podaj liczbe %s: " % (i + 1))
        if type not in types:
            types.add(type)
            i = i + 1