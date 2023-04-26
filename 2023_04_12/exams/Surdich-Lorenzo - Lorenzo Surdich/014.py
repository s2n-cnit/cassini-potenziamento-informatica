def calcola_area():
    figura = input("Che figura vuoi calcolare? (cerchio, quadrato, rettangolo, triangolo)")
    if figura == "cerchio":
        raggio = float(input("Inserisci il raggio del cerchio"))
        area = 3.14 * raggio ** 2
        print(f"L'area del cerchio è {area}")
    elif figura == "quadrato":
        lato = float(input("Inserisci il lato del quadrato"))
        area = lato ** 2
        print(f"L'area del quadrato è {area}")
    elif figura == "rettangolo":
        base = float(input("Inserisci la base del rettangolo"))
        altezza = float(input("Inserisci l'altezza del rettangolo"))
        area = base * altezza
        print(f"L'area del rettangolo è {area}")
    elif figura == "triangolo":
        base = float(input("Inserisci la base del triangolo"))
        altezza = float(input("Inserisci l'altezza del triangolo"))
        area = (base * altezza) / 2
        print(f"L'area del triangolo è {area}")
    else:
        print("Figura non riconosciuta")

calcola_area()