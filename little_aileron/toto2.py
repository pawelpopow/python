import random

number = random.randint(1, 10)
odp = input("Jaką liczbę od 1 do 10 mam na myśli?")

if __name__ == '__main__':
    # print("Wylosowana liczba:", number)
    # print("Podałeś liczbę:", odp)

    if number == int(odp):
        print("Zgadłeś! Dostajesz długopis!")
    else:
        print("Nie zgadłeś! Spróbuj jeszcze raz.")