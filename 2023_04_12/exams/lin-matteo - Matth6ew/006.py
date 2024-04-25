def main():
    inputnum = input('inserire lista numeri:')
    lista = inputnum.split()
    p = 1
    for i in range(len(lista)):
        p = p * float(lista[i])
    print(p)

main()