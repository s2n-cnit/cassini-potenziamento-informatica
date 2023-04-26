def converti_in_secondi():
    giorni = int(input("Inserisci il numero di giorni: "))
    ore = int(input("Inserisci il numero di ore: "))
    minuti = int(input("Inserisci il numero di minuti: "))

    totale_secondi = giorni * 24 * 60 * 60 + ore * 60 * 60 + minuti * 60

    print("Il totale in secondi è:", totale_secondi)

