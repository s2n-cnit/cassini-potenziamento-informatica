# Chiedi ala persona designata tre numeri
numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))
numero3 = float(input("Inserisci il terzo numero: "))

# qual'è il più grande?
if numero1 > numero2 and numero1 > numero3:
    print("Il numero più grande è:", numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("Il numero più grande è:", numero2)
elif numero3 > numero1 and numero3 > numero2:
    print("Il numero più grande è:", numero3)
else:
    print("I numeri sono uguali!")