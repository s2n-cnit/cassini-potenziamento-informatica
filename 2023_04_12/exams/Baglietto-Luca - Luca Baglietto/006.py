if __name__ == '__main__':
    numbers = input("Inserisci una lista di numeri: ").split()
    prd = 1
    for n in numbers:
        prd *= int(n)
    print("Il prodotto è", prd)
