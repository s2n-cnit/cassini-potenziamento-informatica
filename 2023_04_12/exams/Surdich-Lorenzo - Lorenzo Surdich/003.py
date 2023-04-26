numeri = input("Inserisci una lista di numeri separati da uno spazio: ").split() # Chiediamo all'utente di inserire la lista di numeri
maggiore = int(numeri[0]) # Inizializziamo il valore maggiore come il primo numero della lista

for num in numeri: # Iteriamo su tutti i numeri della lista
    if int(num) > maggiore: # Confrontiamo se il numero attuale è maggiore di quello iniziale
        maggiore = int(num) # Se sì, il numero attuale diventa il nuovo maggiore

print("Il maggiore numero della lista è:", maggiore) # Stampiamo il risultato