def mul_list():
    nums = list(map(float, input('List: ').strip().split(',')))
    total = 1
    for n in nums:
        total *= n
        
    print(total)
    
mul_list()