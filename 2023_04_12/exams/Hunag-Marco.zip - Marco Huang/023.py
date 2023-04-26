def salva_canzone():
    # Chiedi all'utente di inserire il titolo e il testo della canzone
    titolo = input("Inserisci il titolo della canzone: ")
    testo = input("Inserisci il testo della canzone: ")

    # Crea il nome del file utilizzando il titolo della canzone
    nome_file = "{}-canzone.txt".format(titolo)

    # Salva il testo della canzone nel file
    with open(nome_file, 'w') as file:
        file.write(testo)

    print("La canzone è stata salvata nel file {}.".format(nome_file))


# Esempio di chiamata alla funzione
salva_canzone()