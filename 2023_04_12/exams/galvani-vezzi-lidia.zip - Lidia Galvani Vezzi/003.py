def max_lista():
    nums = list(map(float, input().strip().split(',')))
    
    m = nums[0]
    for n in nums:
        if n > m:
            m = n
            
    print(m)
    
max_lista()