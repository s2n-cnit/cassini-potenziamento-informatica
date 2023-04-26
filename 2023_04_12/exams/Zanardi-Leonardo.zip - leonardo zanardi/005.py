def sum_list():
    numeri = list(map(float, input('List: ').strip().split(',')))
    risultato = 0
    for n in numeri:
        risultato += n
        
    print(risultato)
    
sum_list()