def in_list():
    x = float(input('Numero: '))
    numeri = list(map(float, input('Elenco: ').strip().split(',')))
    
    if x in numeri:
        print(f'{x} è dentro elenco all indice {numeri.index(x)}')
    else:
        print(f'{x} non è dentro l elenco')
        
in_list()