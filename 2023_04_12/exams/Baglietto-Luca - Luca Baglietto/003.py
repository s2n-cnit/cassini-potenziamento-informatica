if __name__ == '__main__':
    numbers = input("Inserisci una lista di numeri: ").split()
    mx = float("-inf")
    for n in numbers:
        n = int(n)
        if n > mx:
            mx = n
    print("Il massimo è", mx)
