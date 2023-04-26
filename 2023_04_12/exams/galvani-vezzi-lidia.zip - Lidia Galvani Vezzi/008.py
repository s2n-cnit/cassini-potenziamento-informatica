def istogramma():
    nums = list(map(int, input('List: ').strip().split(',')))

    for n in nums:
        print('*' * n)
        
istogramma()