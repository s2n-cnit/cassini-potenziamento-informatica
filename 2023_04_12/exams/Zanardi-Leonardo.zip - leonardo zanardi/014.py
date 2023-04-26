from math import pi

def area():
    shape = int(input('Seleziona cerchio (1), quadrato (2), rettangolo (3) o triangolo (4): '))

    match shape:
        case 1:
            r = float(input('Radius: '))
            a = pi*r*r
        case 2:
            l = float(input('Side: '))
            a = l*l
        case 3:
            l = float(input('Length: '))
            h = float(input('Height: '))
            a = l*h
        case 4:
            b = float(input('Base: '))
            h = float(input('Height: '))
            a = b*h/2
            
    print(a)
    
area()