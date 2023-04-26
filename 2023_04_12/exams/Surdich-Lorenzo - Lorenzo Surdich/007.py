elemento = input("Inserisci l'elemento: ")
lista = input("Inserisci gli elementi della lista separati da uno spazio: ").split()

if elemento in lista:
    print("L'elemento", elemento, "è presente nella lista all'indice", lista.index(elemento))
else:
    print("L'elemento", elemento, "non è presente nella lista")