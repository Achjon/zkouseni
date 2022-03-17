"""
                                                                     /$$                        
                                                                    | $$                        
  /$$$$$$$  /$$$$$$   /$$$$$$$  /$$$$$$        /$$$$$$$$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$$
 /$$_____/ /$$__  $$ /$$_____/ /$$__  $$      |____ /$$/ |____  $$|_  $$_/   /$$__  $$ /$$_____/
|  $$$$$$ | $$  \ $$|  $$$$$$ | $$$$$$$$         /$$$$/   /$$$$$$$  | $$    | $$$$$$$$| $$      
 \____  $$| $$  | $$ \____  $$| $$_____/        /$$__/   /$$__  $$  | $$ /$$| $$_____/| $$      
 /$$$$$$$/| $$$$$$$/ /$$$$$$$/|  $$$$$$$       /$$$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$$|  $$$$$$$
|_______/ | $$____/ |_______/  \_______/      |________/ \_______/   \___/   \_______/ \_______/
          | $$                                                                                  
          | $$                                                                                  
          |__/                                                                                  

Automatické vybíraní studentů ve třídě ke zkoušení
Author: Matěj Gordon
Licence: MIT
"""

import random
import sys
import os
import time

studenti = ['Tobi Antoni', 'Benedikt Jan', 'Beneš Štěpán', 'Bohuslav Martin', 'Budáč Adam', 'Cibulka David', 'Černý Michal', 'Hořejší Tomáš', 'Houska Nicholas Michael', 'Jeřábek Daniel', 'Kilian Jiří Jaroslav', 'Kmeč Marcel', 'Kůrka Matěj', 'Richter Jan', 'Sadílek Jiří', 'Stromšík Vojtěch', 'Suchan Viktor', 'Suchý Adam', 'Süttö Jakub']
zkouseni = []
znamky = []
vyber_loop = True


clear = lambda: os.system('cls')

try:
    vstup_cislo = input("Zadejte počet studentů ke zkoušení: ")
    print("\n")
    vstup_cislo = int(vstup_cislo)
    if vstup_cislo > 19:
        print("error: Zadejte pouze čísla do 19")
        sys.exit(0)
except ValueError:
    print("error: Zadejte pouze čísla")
    sys.exit(0)
clear()    
i = 0
while i < vstup_cislo:
    nahodne_cislo = random.randint(0,len(studenti))
    if studenti[nahodne_cislo-1] not in zkouseni:
        zkouseni.append(studenti[nahodne_cislo-1])
    else:
        vstup_cislo += 1
    i +=1
print(" \n".join(zkouseni))

while vyber_loop == True:
    print("\nCo chcete udělat dále? ")
    print("1 - Pokračovat")
    print("2 - Promíchat pořadí studentů")
    print("3 - Přidat studenta ke zkoušení")
    print("4 - Odebrat studenta ze zkoušení")
    print("5 - Ukončit program")

    vyber = input("Zadejte svůj výběr: ")

    if vyber == "1":
        clear()
        vyber_loop = False
        zkouseni_loop = True
        cislo_zkouseneho = 0
        while zkouseni_loop == True:
            try:               
                znamka = input("Zadejte známku ze zkoušení pro studenta - " + zkouseni[cislo_zkouseneho]+": ")
                znamky.insert(cislo_zkouseneho,znamka)
                cislo_zkouseneho += 1
            except IndexError:
                clear()
                vysledek = "\n".join("{} - {}".format(x, y) for x, y in zip(zkouseni,znamky))
                print("Výsledky: ")
                print(vysledek,"\n")
                f = open("vysledky.txt","w")
                f.write(vysledek)
                f.close()
                print("Výsledky zapsány do souboru!")
                        
                zkouseni_loop = False

    elif vyber == "2": 
        clear()
        random.shuffle(zkouseni)
        print(" \n".join(zkouseni))

    elif vyber == "3":
        clear()
        cislo_vykaz = 1
        zkouseni_pridat = list(set(studenti) - set(zkouseni))
        for student in zkouseni_pridat:
            print(cislo_vykaz,"-",student)
            cislo_vykaz += 1
            
        vybrane_cislo = input("\nVyberte číslo studenta kterého chcete vyzkoušet: ")
        clear()
        print("\nVybrali jste studenta: ",zkouseni_pridat[int(vybrane_cislo)-1])
        print("\nPřidávám studenta do seznamu...")
        time.sleep(0.5)
        clear()
        zkouseni.insert(0,zkouseni_pridat[int(vybrane_cislo)-1])
        print(" \n".join(zkouseni))
        
    elif vyber == "4":
        clear()
        cislo_vykaz = 1
        for student in zkouseni:
            print(cislo_vykaz,"-",student)
            cislo_vykaz += 1
        vybrane_cislo = input("\nVyberte číslo studenta kterého chcete odstanit ze zkoušení: ")
        print("\n")
        clear()
        print("Vybrali jste studenta: ",zkouseni[int(vybrane_cislo)-1])
        print("Odebírám studenta ze seznamu...")
        time.sleep(0.5)
        clear()
        zkouseni.remove(zkouseni[int(vybrane_cislo)-1])
        print(" \n".join(zkouseni))

    elif vyber == "5":
        print("\n")
        vyber_loop = False
    
    else:
        print("\nZadejte prosím validní možnost")