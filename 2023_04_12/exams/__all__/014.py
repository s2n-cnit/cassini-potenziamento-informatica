

# -----------------------
# ./Baglietto-Luca - Luca Baglietto/014.py
#
import math


import math

def cerchio(r):
    print("Area", r*r*math.pi)
    print("Circonferenza" 2*math.pi*r)

def quadrato(l):
    print("Area", l*l)
    print("Perimetro" 4*l)

def rettangolo(a, b):
    print("Area", a*b)
    print("Perimetro", 2*(a+b))

def triangolo(a, b, c):
    p = (a+b+c)/2
    print("Area", math.sqrt(p*(p-a)*(p-b)*(p-c)))
    print("Perimetro" a+b+c)


# -----------------------
# ./roggero_costantino/014.py
#
from math import pi

def area():
    shape = int(input('Select circle (1), square (2), rect (3) or triangle (4): '))

    match shape:
        case 1:
            r = float(input('Radius: '))
            a = pi*r*r
        case 2:
            l = float(input('Side: '))
            a = l*l
        case 3:
            l = float(input('Length: '))
            h = float(input('Height: '))
            a = l*h
        case 4:
            b = float(input('Base: '))
            h = float(input('Height: '))
            a = b*h/2
            
    print(a)
    
area()

# -----------------------
# ./lin-matteo - Matth6ew/014.py
#
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

# -----------------------
# ./Zanardi-Leonardo.zip - leonardo zanardi/014.py
#
from math import pi

def area():
    shape = int(input('Seleziona cerchio (1), quadrato (2), rettangolo (3) o triangolo (4): '))

    match shape:
        case 1:
            r = float(input('Radius: '))
            a = pi*r*r
        case 2:
            l = float(input('Side: '))
            a = l*l
        case 3:
            l = float(input('Length: '))
            h = float(input('Height: '))
            a = l*h
        case 4:
            b = float(input('Base: '))
            h = float(input('Height: '))
            a = b*h/2
            
    print(a)
    
area()

# -----------------------
# ./molinari-giorgia/014.py
#
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

# -----------------------
# ./porcile-filippo.zip - Filippo Porcile/014.py
#
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

# -----------------------
# ./perkola_klaudia - Klaudia Perkola/014.py
#
def geometra():
    print("""
    Benvenuti alla funzione Geometra!
    In fase di selezione, a ciascun possibile calcolo corrisponde un valore numerico:
    - Area Quadrato: 1
    - Area Rettangolo: 2
    - Area Triangolo: 3
    - Area Cerchio: 4
    """)

    print('Dunque. Di quale figura geometrica desideri calcolare l\'area?')
    scelta = int(input(">>> "))
    if scelta == 1:
        print("Hai scelto: Area Quadrato")
        lato = float(input('Inserisci il valore del lato del quadrato '))
        print(f"L'Area del Quadrato, avente lato {lato} è: {lato * lato}")
    elif scelta == 2:
        print("Hai scelto: Area Rettangolo")
        base = float(input('Inserisci il valore della base '))
        altezza = float(input('Inserisci il valore dell´altezza '))
        print(f"L'Area del Rettangolo, avente base {base} e altezza {altezza} è: {base * altezza}")
    elif scelta == 3:
        print("Hai scelto: Area Triangolo")
        base = float(input('Inserisci il valore della base '))
        altezza = float(input('Inserisci il valore dell´altezza '))
        print(f"L'Area del Triangolo, avente base {base} e altezza {altezza} è: {(base * altezza) / 2}")
    elif scelta == 4:
        print("Hai scelto: Area Cerchio")
        r = float(input('Inserisci il valore del raggio '))
        print(f"L'Area del Cerchio, avente raggio {r} è: {(r * r) * 3.14}")
    else:
        print ('Nessun calcolo disponibile per la scelta effettuata!')

# -----------------------
# ./ExamFrittoli - Lorenzo Frittoli/014.py
#
from math import pi

def area():
    shape = int(input('Select circle (1), square (2), rect (3) or triangle (4): '))

    match shape:
        case 1:
            r = float(input('Radius: '))
            a = pi*r*r
        case 2:
            l = float(input('Side: '))
            a = l*l
        case 3:
            l = float(input('Length: '))
            h = float(input('Height: '))
            a = l*h
        case 4:
            b = float(input('Base: '))
            h = float(input('Height: '))
            a = b*h/2
            
    print(a)
    
area()

# -----------------------
# ./alessandro-lugaro/014.py
#
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


# -----------------------
# ./botta-alessio - Alessio Botta/014.py
#
from math import pi

def area():
    shape = int(input('Select circle (1), square (2), rect (3) or triangle (4): '))

    match shape:
        case 1:
            r = float(input('Radius: '))
            a = pi*r*r
        case 2:
            l = float(input('Side: '))
            a = l*l
        case 3:
            l = float(input('Length: '))
            h = float(input('Height: '))
            a = l*h
        case 4:
            b = float(input('Base: '))
            h = float(input('Height: '))
            a = b*h/2
            
    print(a)
    
area()

# -----------------------
# ./esercizi informatica minetti giulio - Giulio Minetti/014.py
#
from math import pi

def area():
    shape = int(input('Select circle (1), square (2), rect (3) or triangle (4): '))

    match shape:
        case 1:
            r = float(input('Radius: '))
            a = pi*r*r
        case 2:
            l = float(input('Side: '))
            a = l*l
        case 3:
            l = float(input('Length: '))
            h = float(input('Height: '))
            a = l*h
        case 4:
            b = float(input('Base: '))
            h = float(input('Height: '))
            a = b*h/2
            
    print(a)
    
area()

# -----------------------
# ./Surdich-Lorenzo - Lorenzo Surdich/014.py
#
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

# -----------------------
# ./todde-lorenzo - lorenzo todde/014.py
#
def calcA():
    poly = input('inserisci il nome della figura: ')
    l = float(input('inserisci la lunghezza del segmento base (base, raggio): '))
    h = float(input("Inserisci l'eventuale altezza: "))
    if poly == 'triangolo':
        print(h * l * .5)
    if poly == 'quadrato':
        print( l * l)
    if poly == 'rettangolo':
        print(l * h)
    if poly == 'cerchio':
        print(l * l * 3.14)
calcA()

# -----------------------
# ./dapino-berenice/014.py
#
def main(): 
    

# -----------------------
# ./portella-francesco - Francesco Portella/014.py
#
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

# -----------------------
# ./moretti-christian/014.py
#
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

# -----------------------
# ./zumiani-sara.zip - Sara Zumiani/014.py
#
from math import pi

def area():
    shape = int(input('Select circle (1), square (2), rect (3) or triangle (4): '))

    match shape:
        case 1:
            r = float(input('Radius: '))
            a = pi*r*r
        case 2:
            l = float(input('Side: '))
            a = l*l
        case 3:
            l = float(input('Length: '))
            h = float(input('Height: '))
            a = l*h
        case 4:
            b = float(input('Base: '))
            h = float(input('Height: '))
            a = b*h/2
            
    print(a)
    
area()

# -----------------------
# ./hu-xuan-di/014.py
#
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

# -----------------------
# ./Hunag-Marco.zip - Marco Huang/014.py
#
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

calcola_area()

# -----------------------
# ./zono veran - Fabrizio Verani/014.py
#
from math import pi

def area():
    shape = int(input('Select circle (1), square (2), rect (3) or triangle (4): '))

    match shape:
        case 1:
            r = float(input('Radius: '))
            a = pi*r*r
        case 2:
            l = float(input('Side: '))
            a = l*l
        case 3:
            l = float(input('Length: '))
            h = float(input('Height: '))
            a = l*h
        case 4:
            b = float(input('Base: '))
            h = float(input('Height: '))
            a = b*h/2
            
    print(a)
    
area()

# -----------------------
# ./galvani-vezzi-lidia.zip - Lidia Galvani Vezzi/014.py
#
from math import pi

def area():
    shape = int(input('Select circle (1), square (2), rect (3) or triangle (4): '))

    match shape:
        case 1:
            r = float(input('Radius: '))
            a = pi*r*r
        case 2:
            l = float(input('Side: '))
            a = l*l
        case 3:
            l = float(input('Length: '))
            h = float(input('Height: '))
            a = l*h
        case 4:
            b = float(input('Base: '))
            h = float(input('Height: '))
            a = b*h/2
            
    print(a)
    
area()

# -----------------------
# ./Matteo-Marazzi/014.py
#
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
