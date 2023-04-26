def main(): 
    a = input("Inserisci il primo numero: ")
    b = input("Inserisci il secondo numero: ")
    c = input("Inserisci il terzo numero: ")
    if a >= b:
        if a >= c:
            print(a)
        elif b >= c:
            print(b)
        else:
            print(c)
    elif b >= c:
        print(b)
    else: 
        print(c)
main()