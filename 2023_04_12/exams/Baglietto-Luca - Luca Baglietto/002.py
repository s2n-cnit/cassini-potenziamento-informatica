if __name__ == '__main__':
    a = int(input("Inserisci il numero a: "))
    b = int(input("Inserisci il numero b: "))
    c = int(input("Inserisci il numero c: "))
    if a > b:
        mx = a
    else:
        mx = b
    if c > mx:
        mx = c
    print("Il massimo è", mx)
