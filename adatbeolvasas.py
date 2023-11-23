def adat():
    # fájl megnyitása beolvasásra
    f = open("adatok.csv", "r")
    # grafikon címe a fájl első sora
    cim = f.readline()
    # táblázat fejlécei
    header = f.readline() + f.readline() + f.readline()
    # táblázat összessége
    adatok = []
    # végig megyek a fájl sorain
    for sor in f:
        adatok.append((sor.replace("..", "0").replace(" ", "").rstrip().split(";")))
        # A sorok listává alakítása és formázása, .. helyett 0, szóközök eltávolítása, majd listában eltárolás
    vezetekes_osszesen = {}  # Létrehozunk dicteket(oszlopok nevei).
    vezetekes_kapcsolt_vonal = {}
    xdsl_halozaton = {}
    kabeltv_halozaton = {}
    optikai_halozaton = {}
    vezetek_nelkuli_halozaton = {}
    osszesen = {}
    for item in adatok:
        # végigmegyek a listákat tartalmazó listán és kiveszem az első elemet ami mindig az évszám,
        # a masodik pedig az oszlophoz tartozó adat
        vezetekes_osszesen[item[0]] = int(item[1])
        vezetekes_kapcsolt_vonal[item[0]] = int(item[2])
        xdsl_halozaton[item[0]] = int(item[3])
        kabeltv_halozaton[item[0]] = int(item[4])
        optikai_halozaton[item[0]] = int(item[5])
        vezetek_nelkuli_halozaton[item[0]] = int(item[6])
        osszesen[item[0]] = int(item[7])
    try:
        # Megpróbáljuk kiírni a szótárak tartalmát.
        print(vezetekes_osszesen)
        print(vezetekes_kapcsolt_vonal)
        print(xdsl_halozaton)
        print(kabeltv_halozaton)
        print(optikai_halozaton)
        print(vezetek_nelkuli_halozaton)
        print(osszesen)
    except FileNotFoundError:
        # Ha a fájl nem található, akkor kiírjuk ezt a hibaüzenetet.
        print("A fajl nem találhato. ")
    except ValueError:
        # Ha a fájlban lévő adatok nem megfelelőek, akkor kiírjuk ezt a hibaüzenetet.
        print("Nem megfelelo adatok a fajlban.")
    except PermissionError:
        # Ha nincs jogosultságunk a fájl megnyitására, akkor kiírjuk ezt a hibaüzenetet.
        print("Nincs jogosultsag a fajl megnyitásara. ")
    except Exception as e:
        # Ha bármilyen más hiba történik, akkor kiírjuk ezt a hibaüzenetet.
        print("Valami hiba tortent: ", e)
    else:
        # Ha nincs hiba, akkor kiírjuk, hogy a fájl sikeresen beolvasva.
        print("A file sikeresen beolvasva. ")
    finally:
        print("A kod veget ert.")
        # Végül kiírjuk, hogy a kód véget ért.
        return vezetekes_osszesen, vezetekes_kapcsolt_vonal, xdsl_halozaton, kabeltv_halozaton, optikai_halozaton, vezetek_nelkuli_halozaton, osszesen



