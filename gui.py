import time
from adatbeolvasas import adat
import pandas as pnd
import matplotlib as plt
# Adatok vezetékes csatlakozásokhoz
def wired():
    print("Hello")

# Adatok a csatlakozási vonali szolgáltatásokhoz
def connection_line():
    pass

# Adatok az XDSL hálózati szolgáltatásokhoz
def XDSL_network():
    pass

# Kábel TV hálózati szolgáltatások adatai
def cable_TV_network():
    pass

# Adatok az optikai hálózati szolgáltatásokhoz
def optical_network():
    pass

# Adatok vezeték nélküli szolgáltatásokhoz
def wireless():
    pass

# Adatok az összes szolgáltatásra vonatkozóan
def total():
    pass

hálózati_szolgáltatások = {
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
    print("Válassza ki a hozzáférési szolgáltatást:")
    for számkód, szolgaltatas in hálózati_szolgáltatások.items():
        print(f"{számkód} - {szolgaltatas}")
    print("0 - Kilepes")

    számkód = input("Adja meg a megtekinteni kivant lekereshez tartozó számot: ")

    if számkód == "0":
        print("Kilépés...")
        time.sleep(1)
        break
    elif számkód in hálózati_szolgáltatások:
        data = None
        if számkód == "1":
            data = wired()
        elif számkód == "2":
            data = connection_line()
        elif számkód == "3":
            data = XDSL_network()
        elif számkód == "4":
            data = cable_TV_network()
        elif számkód == "5":
            data = optical_network()
        elif számkód == "6":
            data = wireless()
        elif számkód == "7":
            data = total()

        print(f"A {hálózati_szolgáltatások[számkód]} hozzáférési szolgáltatásra vonatkozó adatok: {data}")
        print("Ha szeretne kilépni, nyomja meg a '0' gombot!")
        time.sleep(2)
    else:
        print("Hibás szolgáltatás száma! Próbálja újra.")
        time.sleep(2)

        #Comment

