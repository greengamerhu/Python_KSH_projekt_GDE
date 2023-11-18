import time
from adatbeolvasas import adat
import pandas as pnd
import matplotlib as plt
# Adatok vezetekes csatlakozasokhoz
def wired():
    print("Hello")

# Adatok a csatlakozasi vonali szolgaltatasokhoz
def connection_line():
    pass

# Adatok az XDSL halozati szolgaltatasokhoz
def XDSL_network():
    pass

# Kabel TV halozati szolgaltatasok adatai
def cable_TV_network():
    pass

# Adatok az optikai halozati szolgaltatásokhoz
def optical_network():
    pass

# Adatok vezetek nelkuli szolgaltatasokhoz
def wireless():
    pass

# Adatok az osszes szolgaltatasra vonatkozoan
def total():
    pass

halozati_szolgaltatasok = {
    "1": "Vezetekes",
    "2": "Kapcsolt vonal (modem segitsegevel) + ISDN",
    "3": "XDSL halozat",
    "4": "Kabel-tv halozat",
    "5": "Optikai halozat",
    "6": "Vezetek nelkuli",
    "7": "Osszesen"
}
vezetekes_osszesen, vezetekes_kapcsolt_vonal, xdsl_halozaton, kabeltv_halozaton, optikai_halozaton, vezetek_nelkuli_halozaton, osszesen = adat()
print(vezetekes_osszesen)
print(osszesen)

while True:
    print("Valassza ki a hozzaferesi szolgaltatast:")
    for szamkod, szolgaltatas in halozati_szolgaltatasok.items():
        print(f"{szamkod} - {szolgaltatas}")
    print("0 - Kilepes")

    szamkod = input("Adja meg a megtekinteni kivant lekereshez tartozo szamot: ")

    if szamkod == "0":
        print("Kilepes...")
        time.sleep(1)
        break
    elif szamkod in halozati_szolgaltatasok:
        data = None
        if szamkod == "1":
            data = wired()
        elif szamkod == "2":
            data = connection_line()
        elif szamkod == "3":
            data = XDSL_network()
        elif szamkod == "4":
            data = cable_TV_network()
        elif szamkod == "5":
            data = optical_network()
        elif szamkod == "6":
            data = wireless()
        elif szamkod == "7":
            data = total()

        print(f"A {halozati_szolgaltatasok[szamkod]} hozzaferesi szolgaltatasra vonatkozo adatok: {data}")
        print("Ha szeretne kilepni, nyomja meg a '0' gombot!")
        time.sleep(2)
    else:
        print("Hibas szolgaltatas szama! Probálja ujra.")
        time.sleep(2)

        #Comment
        #comment1
