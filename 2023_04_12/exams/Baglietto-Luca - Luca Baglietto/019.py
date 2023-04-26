def trova():
    colors = input("inserisci dieci colori: ").split()
    if len(colors) != 10:
        print("Lunghezzaa invalida")
        return
    c = input("Inserisci una lettera: ")
    for col in colors:
        if col[0] == c:
            print(col)
trova()