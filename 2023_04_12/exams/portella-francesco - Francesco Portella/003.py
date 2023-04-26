def main():
    inputnum = input('inserire lista numeri:')
    lista = inputnum.split()
    for i in range(len(lista)):
        lista[i] = float(lista[i])
    maxnum= lista[0]
    for n in range(len(lista)):
        if maxnum <= lista[n]:
            maxnum = lista[n]
    print(maxnum)

main()