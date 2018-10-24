
#for x in range(1,8):
 #   print(x)
import random

def kpn():
    komputer = random.randint(1,3)
    if kamien == 1:
        kamien()
    elif nozyce == 2:
        nozyce()
    elif papier == 3:
        papier()

def kamien():
    uzytkownik = input("1 - kamien, 2 - nozyce, 3 - papier:" )
    if uzytkownik == "1":
        print("Zremisowales. Ty kamień, komp kamień")
        tryAgain()
    if uzytkownik == "2":
        print("Przegrałeś. Ty nozyczki, komp kamień")
        tryAgain()
    if uzytkownik == "3":
        print("Wygrałeś. Ty papier, komp kamień")
        tryAgain()

def nozyce():
    uzytkownik = input("1 - kamien, 2 - nozyce, 3 - papier:" )
    if uzytkownik == "1":
        print("Wygrałeś. Ty kamień, komp nozyczki")
        tryAgain()
    if uzytkownik == "2":
        print("Zremisowales. Ty nozyczki, komp nozyczki")
        tryAgain()
    if uzytkownik == "3":
        print("Przegrałeś. Ty papier, komp nozyczki")
        tryAgain()

def papier():
    uzytkownik = input("1 - kamien, 2 - nozyce, 3 - papier:" )
    if uzytkownik == "1":
        print("Przegrałeś. Ty kamień, komp papier")
        tryAgain()
    if uzytkownik == "2":
        print("Wygrałeś. Ty nozyczki, komp papier")
        tryAgain()
    if uzytkownik == "3":
        print("Zremisowałeś. Ty papier, komp papier")
        tryAgain()


def tryAgain():
    wybor =input('Zagrasz jeszcze raz? Wpisz tak')
    if wybor == "tak":
          kpn()
    if wybor == "nie":
        quit()

kpn()

   # lista =[1,2,3]
    #a random.choice(lista)
    # print(a)

        