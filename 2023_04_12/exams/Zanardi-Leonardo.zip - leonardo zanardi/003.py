def max_list():
    numeri = list(map(int, input().strip().split(',')))
    
    x = numeri[0]
    for y in numeri:
        if y > x:
            x = y
            
    print(x)
    
max_list()