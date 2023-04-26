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


