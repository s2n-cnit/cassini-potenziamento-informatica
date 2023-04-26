def info_pianeti():
    # Creazione della tupla contenente le informazioni sui pianeti
    pianeti = (
        ("Mercurio", "roccioso", 0),
        ("Venere", "roccioso", 0),
        ("Terra", "roccioso", 1),
        ("Marte", "roccioso", 2),
        ("Giove", "gassoso", 79),
        ("Saturno", "gassoso", 82),
        ("Urano", "gassoso", 27),
        ("Nettuno", "gassoso", 14)
    )

    # Stampa a schermo il contenuto della tupla
    for pianeta in pianeti:
        print("Nome: {}\nTipologia: {}\nNumero di satelliti: {}\n".format(pianeta[0], pianeta[1], pianeta[2]))

    # Calcolo del numero totale di satelliti
    totale_satelliti = sum(pianeta[2] for pianeta in pianeti)
    print("Numero totale di satelliti: {}".format(totale_satelliti))


# Esempio di chiamata alla funzione
info_pianeti()