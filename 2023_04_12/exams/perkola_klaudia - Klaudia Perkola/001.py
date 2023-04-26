#chiedi all'utente di inserire due numeri
a = input("Inserisci il primo numero: ")
b = input("Inserisci il secondo numero: ")

#confronta i due numeri utilizzando le istruzioni if, elif ed else
if a == b:
    print("I numeri sono identici")
elif a > b:
    print("Il numero più grande tra i due è " + str(a))
else:
    print("Il numero più grande tra i due è " + str(b))