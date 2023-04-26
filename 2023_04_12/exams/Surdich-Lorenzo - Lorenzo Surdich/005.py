numeri = input("Inserisci una lista di numeri separati da uno spazio: ").split()
somma = 0

for numero in numeri:
    somma += int(numero)

print("La somma di tutti i numeri è:", somma)