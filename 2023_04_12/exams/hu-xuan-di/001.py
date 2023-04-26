# Chiedi all'utente di inserire due numeri
numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))

# Confronta i due numeri utilizzando le istruzioni if, elif ed else
if numero1 > numero2:
    print("Il numero più grande è:", numero1)
elif numero1 < numero2:
    print("Il numero più grande è:", numero2)
else:
    print("I numeri sono uguali!")