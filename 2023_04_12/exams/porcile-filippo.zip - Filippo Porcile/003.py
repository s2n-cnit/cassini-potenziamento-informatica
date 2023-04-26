# Chiedi all'utente di inserire una lista di numeri separati da spazi
input_numeri = input("Inserisci una lista di numeri separati da spazi: ")

# Suddivide la stringa di input in una lista di stringhe di numeri
lista_numeri = input_numeri.split()

# Converte ciascuna stringa di numero in un numero float
for i in range(len(lista_numeri)):
    lista_numeri[i] = float(lista_numeri[i])

# Inizializza la variabile per il numero più grande con il primo numero della lista
numero_piu_grande = lista_numeri[0]

# Confronta i numeri nella lista per trovare il numero più grande
for numero in lista_numeri:
    if numero > numero_piu_grande:
        numero_piu_grande = numero

# Stampa il numero più grande a schermo
print("Il numero più grande è:", numero_piu_grande)