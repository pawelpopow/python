import random

numberofnumbers = int(input("Podaj ilość typowanych liczb: "))
maxnumber = int(input("Podaj maksymalna losowa liczbe: "))

if __name__ == '__main__':
    # print("Wytypuj %s z %s liczb: " % (numberofnumbers, maxnumber))

    number = []
    # for i in range(numberofnumbers):
    i = 0
    while i < numberofnumbers:
        numbers = random.randint(1, maxnumber)
        if number.count(numbers) == 0:
            number.append(numbers)
            i = i + 1
    print("Wylosowane liczby: ", number)
