def main(): 
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))
    c = float(input("Inserisci il terzo numero: "))
    if a>b: 
        if a>c: 
            print("Numero maggiore:", a)
        else:
            print("Numero maggiore:", c)

    else:
        if b>c:
            print("Numero maggiore:", b)
        else: 
            print("Numero maggiore:", c)



main()