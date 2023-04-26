def mul_list():
    numeri = list(map(float, input('Elenco = ').strip().split(',')))
    risultato = 1
    for n in numeri:
        risultato *= n
        
    print(risultato)
    
mul_list()