input_numeri = input("Inserisci una lista di numeri separati da spazi: ")

lista_numeri = input_numeri.split()

for i in range(len(lista_numeri)):
    lista_numeri[i] = float(lista_numeri[i])

numero_piu_grande = lista_numeri[0]

for numero in lista_numeri:
    if numero > numero_piu_grande:
        numero_piu_grande = numero

print("Il numero più grande è:", numero_piu_grande)