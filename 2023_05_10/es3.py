# Scrivi una funzione Python per rimuovere i duplicati da una lista preservando l’ordine degli elementi al suo interno.

lista = [1, 2, 1, 3, 2, 4, 5]
output = [1, 2, 3, 4, 5]


def rimuovi_duplicati(lista):
    output = []
    for i in range(len(lista) - 1):
        trovato = False
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                trovato = True
                break
        if not trovato:
            output.append(lista[i])
    return output
