import random

number = random.randint(1, 10)

if __name__ == '__main__':
    # print("Wylosowana liczba:", number)

    for i in range(3):
        print("Próba ", i + 1)
        odp = input("Jaką liczbę od 1 do 10 mam na myśli?")
        # print("Podałeś liczbę:", odp)

        if number == int(odp):
            print("Zgadłeś! Dostajesz długopis!")
            break
        elif i == 2:
            print("Miałem na myśli liczbe: ", number)
        else:
            print("Nie zgadłeś! Spróbuj jeszcze raz.")
        print()
