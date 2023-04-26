n1 = float(input("Inserisci il primo numero: "))
n2 = float(input("Inserisci il secondo numero: "))
n3 = float(input("Inserisci il terzo numero: "))

if n1 > n2 and n1 > n3:
    print("Il numero più grande è:", n1)
elif n2 > n1 and n2 > n3:
    print("Il numero più grande è:", n2)
elif n3 > n1 and n3 > n2:
    print("Il numero più grande è:", n3)
