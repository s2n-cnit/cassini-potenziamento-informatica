def istogram():
    numeri = list(map(int, input('List: ').strip().split(',')))

    for x in numeri:
        print('*' * x)
        
istogram()