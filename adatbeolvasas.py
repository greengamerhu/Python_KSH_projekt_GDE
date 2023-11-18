def adat():
    f = open("adatok.csv", "r")
    cim = f.readline()
    header = f.readline() + f.readline() + f.readline()
    adatok = []
    for sor in f:
        adatok.append((sor.replace("..", "0").replace(" ", "").rstrip().split(";")))
    vezetekes_osszesen = {}
    vezetekes_kapcsolt_vonal = {}
    xdsl_halozaton = {}
    kabeltv_halozaton = {}
    optikai_halozaton = {}
    vezetek_nelkuli_halozaton = {}
    osszesen = {}
    for item in adatok:
        vezetekes_osszesen[item[0]] = int(item[1])
        vezetekes_kapcsolt_vonal[item[0]] = int(item[2])
        xdsl_halozaton[item[0]] = int(item[3])
        kabeltv_halozaton[item[0]] = int(item[4])
        optikai_halozaton[item[0]] = int(item[5])
        vezetek_nelkuli_halozaton[item[0]] = int(item[6])
        osszesen[item[0]] = int(item[7])
    try:
        print(vezetekes_osszesen)
        print(vezetekes_kapcsolt_vonal)
        print(xdsl_halozaton)
        print(kabeltv_halozaton)
        print(optikai_halozaton)
        print(vezetek_nelkuli_halozaton)
        print(osszesen)
    except FileNotFoundError:
        print("A fájl nem található. ")
    except ValueError:
        print("Nem megfelelő adatok a fájlban.")
    except PermissionError:
        print("Nincs jogosultság a fájl megnyitására. ")
    except Exception as e:
        print("Valami hiba történt: ", e)
    else:
        print("A file sikeresen beolvasva. ")
    finally:
        print("A kód véget ért.")
        return vezetekes_osszesen, vezetekes_kapcsolt_vonal, xdsl_halozaton, kabeltv_halozaton, optikai_halozaton, vezetek_nelkuli_halozaton, osszesen



