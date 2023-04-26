if __name__ == '__main__':
    numbers = input("Inserisci una lista di numeri: ").split()
    sm = 0
    for n in numbers:
        sm += int(n)
    print("La somma è", sm)
