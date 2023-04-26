def info_pianeti():
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

    for pianeta in pianeti:
        print("Nome: {}\nTipologia: {}\nNumero di satelliti: {}\n".format(pianeta[0], pianeta[1], pianeta[2]))

    totale_satelliti = sum(pianeta[2] for pianeta in pianeti)
    print("Numero totale di satelliti: {}".format(totale_satelliti))


info_pianeti()