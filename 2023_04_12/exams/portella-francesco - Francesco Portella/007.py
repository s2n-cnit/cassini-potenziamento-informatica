def main():
    input_lista = input('inserisci lista di oggetti separati da "spazio": ')
    list = input_lista.split()
    thing = input('inserisci un elemento da cercare: ')
    if thing in list:
        print("L'elemento è presente nella posizione " + str(list.index(thing)))
    else:
        print("L'elemento non è presente")

main()
