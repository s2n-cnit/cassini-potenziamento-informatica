def salva_canzone():
    titolo = input("Inserisci il titolo della canzone: ")
    testo = input("Inserisci il testo della canzone: ")

    nome_file = "{}-canzone.txt".format(titolo)

    with open(nome_file, 'w') as file:
        file.write(testo)

    print("La canzone è stata salvata nel file {}.".format(nome_file))


salva_canzone()