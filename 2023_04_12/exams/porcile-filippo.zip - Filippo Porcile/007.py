# Definisci la lista di elementi
lista_elementi = ['apple', 'banana', 'cherry', 'date', 'fig']

# Chiedi all'utente di inserire un elemento da cercare
elemento = input("Inserisci un elemento da cercare nella lista: ")

# Utilizza il metodo index() per cercare l'elemento nella lista
# Se l'elemento è presente, restituisce l'indice, altrimenti solleva un'eccezione ValueError
try:
    indice = lista_elementi.index(elemento)
    print("L'elemento", elemento, "è presente nella lista all'indice", indice)
except ValueError:
    print("L'elemento", elemento, "non è presente nella lista.")