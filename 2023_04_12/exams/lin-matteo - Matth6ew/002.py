def main():
    a = float(input('primo numero:'))
    b = float(input('secondo numero:'))
    c = float(input('terzo numero:'))
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >=c :
        print(b)
    else:
        print(c)

main()