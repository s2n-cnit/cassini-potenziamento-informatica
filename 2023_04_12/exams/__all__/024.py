

# -----------------------
# ./roggero_costantino/024.py
#
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

# -----------------------
# ./lin-matteo - Matth6ew/024.py
#
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

# -----------------------
# ./Zanardi-Leonardo.zip - leonardo zanardi/024.py
#
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

# -----------------------
# ./molinari-giorgia/024.py
#
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

# -----------------------
# ./porcile-filippo.zip - Filippo Porcile/024.py
#
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

# -----------------------
# ./perkola_klaudia - Klaudia Perkola/024.py
#
pianeti = (
    ("Mercurio", "roccioso", 0),
    ("Venere", "roccioso", 0),
    ("Terra", "roccioso", 1),
    ("Marte", "roccioso", 2),
    ("Giove", "gassoso", 95),
    ("Saturno", "gassoso", 83),
    ("Urano", "gassoso", 27),
    ("Nettuno", "gassoso", 14)
)
def info_pianeti():
    # Stampa a schermo il contenuto della tupla
    print("I pianeti del sistema solare sono:")
    for pianeta in pianeti:
        print(f"{pianeta[0]}: {pianeta[1]}, {pianeta[2]} satelliti")

    # Calcola il numero totale di satelliti naturali
    num_satelliti = sum([pianeta[2] for pianeta in pianeti])

    # Stampa a schermo il numero totale di satelliti naturali
    print(f"Il numero totale di satelliti naturali conosciuti nel sistema solare è di {num_satelliti}")

info_pianeti()

# -----------------------
# ./alessandro-lugaro/024.py
#
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

# -----------------------
# ./Surdich-Lorenzo - Lorenzo Surdich/024.py
#
def sistema_solare():
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
satelliti_totali = sum([p[2] for p in pianeti])
print("Il sistema solare contiene i seguenti pianeti:")
for p in pianeti:
    print("- {} ({}, {} satelliti)".format(p[0], p[1], p[2]))
print("Il numero totale di satelliti naturali conosciuti nel sistema solare è:", satelliti_totali)




# -----------------------
# ./portella-francesco - Francesco Portella/024.py
#
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

# -----------------------
# ./moretti-christian/024.py
#
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

# -----------------------
# ./zumiani-sara.zip - Sara Zumiani/024.py
#


# -----------------------
# ./hu-xuan-di/024.py
#
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

# -----------------------
# ./Hunag-Marco.zip - Marco Huang/024.py
#


# -----------------------
# ./zono veran - Fabrizio Verani/024.py
#
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

# -----------------------
# ./galvani-vezzi-lidia.zip - Lidia Galvani Vezzi/024.py
#


# -----------------------
# ./Matteo-Marazzi/024.py
#
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