def max_list():
    nums = list(map(int, input().strip().split(',')))
    
    m = nums[0]
    for n in nums:
        if n > m:
            m = n
            
    print(m)
    
max_list()