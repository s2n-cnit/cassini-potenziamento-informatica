lista_elementi = ['banana', 'book', 'computer', 'home']

elemento = input("Inserisci un elemento da cercare nella lista: ")

try:
    indice = lista_elementi.index(elemento)
    print("L'elemento", elemento, "è presente nella lista all'indice", indice)
except ValueError:
    print("L'elemento", elemento, "non è presente nella lista.")