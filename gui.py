import time
from adatbeolvasas import adat
import numpy as np
import matplotlib.pyplot as plt
vezetekes_osszesen, vezetekes_kapcsolt_vonal, xdsl_halozaton, kabeltv_halozaton, optikai_halozaton, vezetek_nelkuli_halozaton, osszesen = adat()

# Adatok vezetekes csatlakozasokhoz
def wired():
    plt.ticklabel_format(style='plain') # az y tengelyen megjeleno adatok formajanak beallitasa
    plt.title("Vezetékes hálózatok alakulása") # a grafikon nevet bealitom
    #xy tengelyek felcimkezese
    plt.ylabel("előfizetések száma")
    plt.xlabel("Év")
    #a grafikon adatainak megadasa
    plt.plot(vezetekes_osszesen.keys(), vezetekes_osszesen.values())
    plt.show()
    tablazat = ""
    for item in kabeltv_halozaton.items():
        tablazat += '\n'+ str(item)
    return tablazat
# Adatok a csatlakozasi vonali szolgaltatasokhoz
def connection_line():
    plt.ticklabel_format(style='plain') # az y tengelyen megjeleno adatok formajanak beallitasa
    plt.title("A kapcsolt vezetékes hálózatok alakulása") # a grafikon nevet bealitom
    #xy tengelyek felcimkezese
    plt.ylabel("előfizetések száma")
    plt.xlabel("Év")
    #a grafikon adatainak megadasa
    plt.plot(vezetekes_kapcsolt_vonal.keys(), vezetekes_kapcsolt_vonal.values())
    plt.show()
    tablazat = ""
    for item in vezetekes_kapcsolt_vonal.items():
        tablazat += '\n'+ str(item)
    return tablazat

# Adatok az XDSL halozati szolgaltatasokhoz
def XDSL_network():
    plt.ticklabel_format(style='plain') # az y tengelyen megjeleno adatok formajanak beallitasa
    plt.title("Az XDSL vezetékes hálózatok alakulása") # a grafikon nevet bealitom
    #xy tengelyek felcimkezese
    plt.ylabel("előfizetések száma")
    plt.xlabel("Év")
    #a grafikon adatainak megadasa
    plt.plot(xdsl_halozaton.keys(), xdsl_halozaton.values())
    plt.show()
    tablazat = ""
    for item in xdsl_halozaton.items():
        tablazat += '\n'+ str(item)
    return tablazat
# Kabel TV halozati szolgaltatasok adatai
def cable_TV_network():
    plt.ticklabel_format(style='plain') # az y tengelyen megjeleno adatok formajanak beallitasa
    plt.title("A kábel-TV kapcsolatos hálózatok alakulása")  # a grafikon nevet bealitom
    # xy tengelyek felcimkezese
    plt.ylabel("előfizetések száma")
    plt.xlabel("Év")
    # a grafikon adatainak megadasa
    plt.plot(kabeltv_halozaton.keys(), kabeltv_halozaton.values())
    plt.show()
    tablazat = ""
    for item in kabeltv_halozaton.items():
        tablazat += '\n'+ str(item)
    return tablazat
# Adatok az optikai halozati szolgaltatásokhoz
def optical_network():
    plt.ticklabel_format(style='plain')  # az y tengelyen megjeleno adatok formajanak beallitasa
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
    plt.ticklabel_format(style='plain')  # az y tengelyen megjeleno adatok formajanak beallitasa
    plt.title("A vezeték nélküli hálózatok alakulása")  # a grafikon nevet bealitom
    # xy tengelyek felcimkezese
    plt.ylabel("előfizetések száma")
    plt.xlabel("Év")
    # a grafikon adatainak megadasa
    plt.plot(vezetek_nelkuli_halozaton.keys(), vezetek_nelkuli_halozaton.values())
    plt.show()
    tablazat = ""
    for item in vezetek_nelkuli_halozaton.items():
        tablazat += '\n'+ str(item)
    return tablazat

# Adatok az osszes szolgaltatasra vonatkozoan
def total():
    plt.ticklabel_format(style='plain')  # az y tengelyen megjeleno adatok formajanak beallitasa
    plt.title("Az internet hozzáférés alakulása")  # a grafikon nevet bealitom
    # xy tengelyek felcimkezese
    plt.ylabel("előfizetések száma")
    plt.xlabel("Év")
    # a grafikon adatainak megadasa
    plt.plot(osszesen.keys(), osszesen.values())
    plt.show()
    tablazat = ""
    for item in osszesen.items():
        tablazat += '\n'+ str(item)
    return tablazat
def wired_technologies_compared():
    plt.ticklabel_format(style='plain')  # az y tengelyen megjeleno adatok formajanak beallitasa
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
    plt.ticklabel_format(style='plain')  # az y tengelyen megjeleno adatok formajanak beallitasa
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

#regreszio

def linear_regression():
    plt.ticklabel_format(style='plain')
    plt.title("Az internet hozzáférés alakulása trend vonallal")  # a grafikon nevet bealitom
    # xy tengelyek felcimkezese
    plt.ylabel("előfizetések száma")
    plt.xlabel("Év")

    plot_x = []
    #Mivel szorozni nem igazán lehet string-el ezért kénytelen voltam átalakítani
    for i in osszesen.keys():
        plot_x.append(int(i))
    plot_y = list(osszesen.values())
    coef = np.polyfit(plot_x, plot_y, 1)
    y_pred = []
    for i in plot_x:
        y_pred.append(coef[0] * i + coef[1])
    # a grafikon adatainak megadasa
    plt.xticks(plot_x)  # az x tengely egészek megjelenítésére rákényszerítése
    plt.plot(plot_x, plot_y, label="Internetes előfizetések alakulása")
    plt.plot(plot_x, y_pred, label="Lineáris Regresszió")
    plt.legend()
    print("A 2024-es várható előfizetések száma: {:.2f}".format(coef[0] * 2023 + coef[1]))
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
    "9" : "2022 minden halozat osszevetve",
    "10" : "lineáris regresszio"
}

def startProgram():
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
            elif szamkod == "10":
                data = linear_regression()
            if(szamkod == "8" or szamkod == "9"):
                print("Ha szeretne kilepni, nyomja meg a '0' gombot!")
            else:
                print(f"A {halozati_szolgaltatasok[szamkod]} hozzaferesi szolgaltatasra vonatkozo adatok: {data}")
                print("Ha szeretne kilepni, nyomja meg a '0' gombot!")
            time.sleep(2)
        else:
            print("Hibas szolgaltatas szama! Probálja ujra.")
            time.sleep(2)

        #Comment
        #comment1
        #comment
