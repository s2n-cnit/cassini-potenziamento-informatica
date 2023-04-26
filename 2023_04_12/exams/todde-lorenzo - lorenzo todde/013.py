def sec():
    days = float(input('Inserisci numero di giorni: '))
    hours = float(input('Inserisci numero di ore: '))
    minutes = float(input('Inserisci numero di minuti: '))
    sectot = (((days*24 + hours)*60) + minutes)*60
    print(sectot)
sec()