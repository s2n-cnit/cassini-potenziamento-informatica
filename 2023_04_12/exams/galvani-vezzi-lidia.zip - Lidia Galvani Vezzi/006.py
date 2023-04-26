def moltiplic():
    nums = list(map(float, input('List: ').strip().split(',')))
    total = 1
    for n in nums:
        total *= n
        
    print(total)
    
moltiplic()