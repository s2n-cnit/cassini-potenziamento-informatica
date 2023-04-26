import math

def calcola_area():
    print("Seleziona la forma geometrica:")
    print("1. Cerchio")
    print("2. Quadrato")
    print("3. Rettangolo")
    print("4. Triangolo")
    
    scelta = int(input("Inserisci il numero corrispondente alla forma geometrica scelta: "))

    if scelta == 1:
        raggio = float(input("Inserisci il raggio del cerchio: "))
        area = math.pi * raggio**2
        print("L'area del cerchio è:", area)
    elif scelta == 2:
        lato = float(input("Inserisci il lato del quadrato: "))
        area = lato**2
        print("L'area del quadrato è:", area)
    elif scelta == 3:
        base = float(input("Inserisci la base del rettangolo: "))
        altezza = float(input("Inserisci l'altezza del rettangolo: "))
        area = base * altezza
        print("L'area del rettangolo è:", area)
    elif scelta == 4:
        base = float(input("Inserisci la base del triangolo: "))
        altezza = float(input("Inserisci l'altezza del triangolo: "))
        area = 0.5 * base * altezza
        print("L'area del triangolo è:", area)
    else:
        print("Scelta non valida. Riprova.")