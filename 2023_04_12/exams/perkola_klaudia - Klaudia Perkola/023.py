def salva_testo_canzone(titolo, testo):
    nome_file = titolo + '.txt'
    with open(nome_file, 'w') as file_testo:
        file_testo.write(testo)
    print(f"Testo della canzone '{titolo}' salvato in '{nome_file}'.")

titolo_canzone = input("Inserisci il titolo della canzone: ")
testo_canzone = input("Inserisci il testo della canzone: ")

salva_testo_canzone(titolo_canzone, testo_canzone)