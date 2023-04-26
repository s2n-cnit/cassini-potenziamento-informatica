def max_3():
    x = float(input('first number: '))
    y = float(input('second number: '))
    z= float(input('third number: '))
    
    if x > y and x > z:
        print(x)
    elif y > x and y > z:
        print(y)
    else:
        print(z)
        
max_3()