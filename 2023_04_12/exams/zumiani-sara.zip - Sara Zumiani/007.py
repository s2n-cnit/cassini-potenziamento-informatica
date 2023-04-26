def el_list():
    a = float(input('Number: '))
    nums = list(map(float, input('List: ').strip().split(',')))
    
    if a in nums:
        print(f'{a} is in the list at index {nums.index(a)}')
    else:
        print(f'{a} is not in the list')
        
el_list()