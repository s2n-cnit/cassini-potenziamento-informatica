if __name__ == '__main__':
    elements = input("Inserisci una lista: ").split()
    element = input("Controlla se un elemento è nella lista: ")
    if element in elements:
        print("Elemento trovato all'indice", elements.index(element), "(Gli indici prtono da 0).")
    else:
        print("Elamento non trovato")
