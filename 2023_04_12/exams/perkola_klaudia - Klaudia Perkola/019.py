def colori():
    colors = []
    for _ in range(10):
        color = input("Inserisci un colore: ")
        colors.append(color)

    #chiedi all'utente di inserire una lettera
    letter = input("Inserisci una lettera: ")

    return [color for color in colors if color.startswith(letter)]

colori()