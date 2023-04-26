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