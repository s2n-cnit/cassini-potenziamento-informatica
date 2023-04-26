def is_perfect(num: int):
    divs = 0
    for n in range(num-1):
        if num%(n+1) == 0:
            divs += (n+1)
            
    if divs == num:
        print(f'{num} is a perfect number')
    else:
        print(f'{num} is not a perfect number')