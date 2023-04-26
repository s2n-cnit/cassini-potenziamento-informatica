#chiedi all'utente di inserire tre numeri
a = input("Inserisci il primo numero: ")
b = input("Inserisci il secondo numero: ")
c = input("Inserisci il terzo numero: ")

#confronta i tre numeri utilizzando le istruzioni if, elif ed else
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
elif c >= a and c >= b:
    print(c)