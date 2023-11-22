import time
from adatbeolvasas import adat
import pandas as pnd
import matplotlib.pyplot as plt
plt.ticklabel_format(style='plain') # az y tengelyen megjeleno adatok formajanak beallitasa
vezetekes_osszesen, vezetekes_kapcsolt_vonal, xdsl_halozaton, kabeltv_halozaton, optikai_halozaton, vezetek_nelkuli_halozaton, osszesen = adat()

# Adatok vezetekes csatlakozasokhoz
def wired():
    plt.title("Vezetékes hálózatok alakulása") # a grafikon nevet bealitom
    #xy tengelyek felcimkezese
    plt.ylabel("előfizetések száma")
    plt.xlabel("Év")
    #a grafikon adatainak megadasa
    plt.plot(vezetekes_osszesen.keys(), vezetekes_osszesen.values())
    plt.show()

# Adatok a csatlakozasi vonali szolgaltatasokhoz
def connection_line():
    plt.title("A kapcsolt vezetékes hálózatok alakulása") # a grafikon nevet bealitom
    #xy tengelyek felcimkezese
    plt.ylabel("előfizetések száma")
    plt.xlabel("Év")
    #a grafikon adatainak megadasa
    plt.plot(vezetekes_kapcsolt_vonal.keys(), vezetekes_kapcsolt_vonal.values())
    plt.show()

# Adatok az XDSL halozati szolgaltatasokhoz
def XDSL_network():
    plt.title("Az XDSL vezetékes hálózatok alakulása") # a grafikon nevet bealitom
    #xy tengelyek felcimkezese
    plt.ylabel("előfizetések száma")
    plt.xlabel("Év")
    #a grafikon adatainak megadasa
    plt.plot(xdsl_halozaton.keys(), xdsl_halozaton.values())
    plt.show()

# Kabel TV halozati szolgaltatasok adatai
def cable_TV_network():
    plt.ticklabel_format(style='plain') # eddigre valamiert elfelejtette azt hogy en ezt beallítottam neki.....
    plt.title("A kábel-TV kapcsolatos hálózatok alakulása")  # a grafikon nevet bealitom
    # xy tengelyek felcimkezese
    plt.ylabel("előfizetések száma")
    plt.xlabel("Év")
    # a grafikon adatainak megadasa
    plt.plot(kabeltv_halozaton.keys(), kabeltv_halozaton.values())
    plt.show()

# Adatok az optikai halozati szolgaltatásokhoz
def optical_network():
    plt.ticklabel_format(style='plain')
    plt.title("Az optikai hálózatok alakulása")  # a grafikon nevet bealitom
    # xy tengelyek felcimkezese
    plt.ylabel("előfizetések száma")
    plt.xlabel("Év")
    # a grafikon adatainak megadasa
    plt.plot(optikai_halozaton.keys(), optikai_halozaton.values())
    plt.show()
    tablazat = ""
    for item in optikai_halozaton.items():
        tablazat += '\n'+ str(item)
    return tablazat

# Adatok vezetek nelkuli szolgaltatasokhoz
def wireless():
    plt.title("A vezeték nélküli hálózatok alakulása")  # a grafikon nevet bealitom
    # xy tengelyek felcimkezese
    plt.ylabel("előfizetések száma")
    plt.xlabel("Év")
    # a grafikon adatainak megadasa
    plt.plot(vezetek_nelkuli_halozaton.keys(), vezetek_nelkuli_halozaton.values())
    plt.show()

# Adatok az osszes szolgaltatasra vonatkozoan
def total():
    plt.title("Az internet hozzáférés alakulása")  # a grafikon nevet bealitom
    # xy tengelyek felcimkezese
    plt.ylabel("előfizetések száma")
    plt.xlabel("Év")
    # a grafikon adatainak megadasa
    plt.plot(osszesen.keys(), osszesen.values())
    plt.show()
def wired_technologies_compared():
    plt.title("A különböző vezetékes hálózatok alakulása") # a grafikon nevet bealitom
    #xy tengelyek felcimkezese
    plt.ylabel("előfizetések száma")
    plt.xlabel("Év")
    #a grafikon adatainak megadasa, bealitom a színét a vonalaknak és cimkeket
    plt.plot(vezetekes_kapcsolt_vonal.keys(), vezetekes_kapcsolt_vonal.values(), color="r", label="vezetekes kapcsolt vonal")
    plt.plot(xdsl_halozaton.keys(), xdsl_halozaton.values(), color="g", label="XDSL")
    plt.plot(kabeltv_halozaton.keys(), kabeltv_halozaton.values(), color="b", label="Kábel Tv")
    plt.plot(optikai_halozaton.keys(), optikai_halozaton.values(), color="c", label="Optikai")
    plt.legend()
    plt.show()
def all_networks_compared_2022_barchart():
    plt.ticklabel_format(style='plain')
    year = str(2022)
    dataByYear = {
        "VezetekesKapcsolt" :  vezetekes_kapcsolt_vonal.get(year),
        "XDSL" : xdsl_halozaton.get(year),
        "KabelTV" : kabeltv_halozaton.get(year),
        "Optikai" : optikai_halozaton.get(year),
        "VezetekNelkuli":  vezetek_nelkuli_halozaton.get(year)
    }
    barplot = plt.bar(dataByYear.keys(), dataByYear.values())
    plt.bar_label(barplot, dataByYear.values())
    plt.show()

halozati_szolgaltatasok = {
    "1": "Vezetekes",
    "2": "Kapcsolt vonal (modem segitsegevel) + ISDN",
    "3": "XDSL halozat",
    "4": "Kabel-tv halozat",
    "5": "Optikai halozat",
    "6": "Vezetek nelkuli",
    "7": "Osszesen",
    "8" : "A vezetékes halozatok alakulasa osszevetve",
    "9" : "2022 minden halozat osszevetve"
}


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
        elif szamkod == "8":
            data = wired_technologies_compared()
        elif szamkod == "9":
            data = all_networks_compared_2022_barchart()

        print(f"A {halozati_szolgaltatasok[szamkod]} hozzaferesi szolgaltatasra vonatkozo adatok: {data}")
        print("Ha szeretne kilepni, nyomja meg a '0' gombot!")
        time.sleep(2)
    else:
        print("Hibas szolgaltatas szama! Probálja ujra.")
        time.sleep(2)

        #Comment
        #comment1
