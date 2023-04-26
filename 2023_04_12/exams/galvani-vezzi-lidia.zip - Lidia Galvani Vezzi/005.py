def somma():
    nums = list(map(float, input('List: ').strip().split(',')))
    total = 0
    for n in nums:
        total += n
        
    print(total)
    
somma()