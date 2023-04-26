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