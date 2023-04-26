def max_3():
    a = float(input('1st number: '))
    b = float(input('2nd number: '))
    c = float(input('3rd number: '))
    
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)
        
max_3()