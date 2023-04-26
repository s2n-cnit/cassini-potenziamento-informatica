numeri = input("Inserisci una serie di numeri separati da spazi: ").split()

risultato = 1  

for numero in numeri:
    risultato *= int(numero) 
print("Il prodotto dei numeri inseriti è:", risultato)