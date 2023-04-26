def main(): 
    num = list(map(float, input().split(',')))

    m = num[0]
    for n in num: 
        if n>m: 
            m=n
        
    print(m)



main()
